<?php
include "phpqrcode.php";

function main_handler($event, $context) {
    $event = json_decode(json_encode($event), true);
    $context = json_decode(json_encode($context), true);
    echo "<!--".json_encode($event)."-->";
    $function_name = $context['function_name'];
    $host_name = $event['headers']['host'];
    $serviceId = $event['requestContext']['serviceId'];
    if ( $serviceId === substr($host_name,0,strlen($serviceId)) ) {
        $path = substr($event['path'], strlen('/' . $function_name . '/')); // When using the API Gateway long link. 使用API网关长链接时
    } else {
        $path = substr($event['path'], strlen($event['requestContext']['path'])); // When using a custom domain name. 使用自定义域名时
    }
    $_GET = $event['queryString'];
    $_POSTbody = explode("&",$event['body']);
    foreach ($_POSTbody as $postvalues){
        $tmp=explode("=",$postvalues);
        $_POST[$tmp[0]]=$tmp[1];
    }
    $value = $_POST['key']; // Give priority to the value submitted by the form POST. 取表格POST提交的值，优先
    if($value == "") $value = key($_GET); // Take the value submitted by '?queryString' after the link. 取链接后?queryString提交的值
    if($value == "") $value = $path; // Directly fetch the value of the non-domain name part of the link. 直接取链接后非域名部分的值

    @ob_start();
?>
<!DOCTYPE html>
<head>
    <title>Generate QR code</title>
    <meta charset=utf-8>
    <meta name="viewport" content="width=device-width,initial-scale=1"/>
</head>
<body>
<table>
    <form name="form1" method="POST" action="">
        <tr>
            <td><textarea name="key" cols="45" rows="8"><?php echo $value;?></textarea></td>
            <td><input name="Submit1" type="submit" value="Generate QR code"></td>
        </tr>
    </form>
</table>
<?php
if($value != ""){
    $value=urldecode($value);
    $logo = __DIR__ . '/logo.png'; // Referring to resources uploaded to SCF. 对上传到SCF的资源的引用
    $remoteaddr=str_replace(":","_",$event['requestContext']['sourceIp']); // IPV6 processing. 以后IPV6的处理
    $QR = "/tmp/".date("Ymd-His")."-".$remoteaddr."-base.png"; // Using '/tmp' temporary folder. 对tmp临时文件夹的使用
    $base = $QR;
    $last = "/tmp/".date("Ymd-His")."-".$remoteaddr."-last.png";
    $errorCorrectionLevel = 'H';
    $matrixPointSize = 15; 
    QRcode::png($value, $QR, $errorCorrectionLevel, $matrixPointSize, 1, $color1); // Generating a QR code image without LOGO and put it in '$QR'. 生成不带LOGO的二维码图片,放在$QR中

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

    imagepng($QR,$last); // Generating the final file and put it in '$last'. 生成最终的文件，放在$last中
    echo '<img src="'. base64EncodeImage($last) .'">';

    unlink($last);
    unlink($base);
}
?>
</body>
</html>
<?php
    // Return a html page. 返回html网页
    $html=ob_get_clean();
    $statusCode=200;
    $isBase64Encoded = false;
    $headers = ['Content-Type' => 'text/html'];
    $value="";
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
