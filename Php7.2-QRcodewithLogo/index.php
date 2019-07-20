<?php
include "phpqrcode.php";

function main_handler($event, $context) {
	$event = json_decode(json_encode($event), true);
    $_GET = $event['queryString'];
    $_PATH = substr($event['path'], strlen($event['requestContext']['path']));
    $_POSTbody = explode("&",$event['body']);
    foreach ($_POSTbody as $postvalues){
        $tmp=explode("=",$postvalues);
        $_POST[$tmp[0]]=$tmp[1];
    }
    $value = $_POST['key']; // 取表格POST提交的值
    if($value == ""){
        $value = key($_GET); // 取链接后?queryString提交的值
    }
    if($value == ""){
        $value = $_PATH; // 直接取链接后非域名部分的值
    }
    $value=urldecode($value);

    @ob_start();
?>
<!DOCTYPE html>
<head>
    <title>二维码</title>
    <meta charset=utf-8>
    <meta name="viewport" content="width=device-width,initial-scale=1"/>
</head>
<body>
<table>
    <form name="form1" method="POST" action="">
        <tr>
            <td><textarea name="key" cols="45" rows="8"><?php echo $value;?></textarea></td>
            <td><input name="Submit1" type="submit" value="生成二维码"></td>
        </tr>
    </form>
</table>
<?php
if($value != ""){
    $logo = __DIR__ . '/logo.png'; // 对上传到SCF的资源的引用
    $remoteaddr=str_replace(":","_",$event['requestContext']['sourceIp']); // 以后IPV6的处理
    $QR = "tmp/".date("Ymd-His")."-".$remoteaddr."-base.png"; // 生成不带LOGO的二维码图片，对tmp临时文件夹的使用
    $base = $QR;
    $last = "tmp/".date("Ymd-His")."-".$remoteaddr."-last.png"; // 最终生成的图片
    $errorCorrectionLevel = 'H';
    $matrixPointSize = 15; 
    QRcode::png($value, $QR, $errorCorrectionLevel, $matrixPointSize, 1, $color1);

    $QR = imagecreatefromstring(file_get_contents($QR));  
    $logo = imagecreatefromstring(file_get_contents($logo)); 
    $QR_width = imagesx($QR);  
    $QR_height = imagesy($QR);  
    $logo_width = imagesx($logo);  
    $logo_height = imagesy($logo);  
    $logo_qr_width = $QR_width / 2.2;
    $scale = $logo_width / $logo_qr_width;
    $logo_qr_height = $logo_height / $scale;  
    $from_width = ($QR_width - $logo_qr_width) / 2;  
    $from_height = ($QR_height - $logo_qr_height) / 2;
    imagecopyresampled($QR, $logo, $from_width, $from_height, 0, 0, $logo_qr_width, $logo_qr_height, $logo_width, $logo_height);

    imagepng($QR,$last); // 生成最终的文件
    echo '<img src="'. base64EncodeImage($last) .'">';

    unlink($last);
    unlink($base);
}
?>
</body>
</html>
<?php
    // 返回html网页
    $html=ob_get_clean();
    $statusCode=200;
    $isBase64Encoded = false;
    $headers = ['Content-Type' => 'text/html'];
    $value="";
    echo "\n<!--".json_encode($event)."-->\n";
    return [
        'isBase64Encoded' => $isBase64Encoded,
        'statusCode' => $statusCode,
        'headers' => $headers,
        'body' => $html
    ];
}

function base64EncodeImage ($image_file) {
  $base64_image = '';
  $image_info = getimagesize($image_file);
  $image_data = fread(fopen($image_file, 'r'), filesize($image_file));
  $base64_image = 'data:' . $image_info['mime'] . ';base64,' . chunk_split(base64_encode($image_data));
  return $base64_image;
}
