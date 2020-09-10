<?php
// include php file
// 對php文件的包含
include "phpqrcode.php";

// main function, called by SCF
// 主函數，調用的入口
function main_handler($event, $context) {
    // print parameters
    // 進門列印傳入參數是好習慣
    echo 'event:'.json_encode($event, JSON_PRETTY_PRINT).'
context:'.json_encode($context, JSON_PRETTY_PRINT);

    // echo $event->{'headers'}->{'host'} ; // parameter is object. 傳入的參數是object

    // convert parameters to array
    // 轉換爲數組
    $event = json_decode(json_encode($event), true);
    $context = json_decode(json_encode($context), true);

    // good choice to clean variables
    // SCF中使用全局的變量前最好清空
    unset($_GET);
    unset($_POST);

    // get the path in url
    // 取得連結中非域名部分的path值
    $function_name = $context['function_name'];
    $host_name = $event['headers']['host'];
    $serviceId = $event['requestContext']['serviceId'];
    if ( $serviceId === substr($host_name,0,strlen($serviceId)) ) {
        // using long url of API gateway
        // 使用API閘道長連結時
        $path = substr($event['path'], strlen('/' . $function_name . '/')); 
    } else {
        // using custom domain
        // 使用自定義域名時
        $path = substr($event['path'], strlen($event['requestContext']['path']=='/'?'/':$event['requestContext']['path'].'/')); 
    }

    // get the queryString
    // 取得連結後?queryString提交的值
    $_GET = $event['queryString'];

    // get the POST values
    // 取得表格POST提交的值
    $_POSTbody = explode("&",$event['body']);
    foreach ($_POSTbody as $postvalues){
        $pos = strpos($postvalues,"=");
        $_POST[urldecode(substr($postvalues,0,$pos))]=urldecode(substr($postvalues,$pos+1));
    }

    $value = $_POST['key'];
    if ($value=='') $value = $path;

    if ($value != '') {
        $logo = __DIR__ . '/logo.png'; // use resource in SCF. 對上傳到SCF的資源的引用
        $remoteaddr=str_replace(":","_",$event['requestContext']['sourceIp']);
        $base = "/tmp/".date("Ymd-His")."-".$remoteaddr."-base.png"; // use the /tmp folder. 對/tmp臨時文件夾的使用
        $QR = $base;
        $last = "/tmp/".date("Ymd-His")."-".$remoteaddr."-last.png";

        // start Generate QRcode
        $errorCorrectionLevel = 'H';
        $matrixPointSize = 15; 
        QRcode::png($value, $QR, $errorCorrectionLevel, $matrixPointSize, 1, $color1);
        $QR = imagecreatefromstring(file_get_contents($QR));
        $logo = imagecreatefromstring(file_get_contents($logo));
        $QR_width = imagesx($QR);
        $QR_height = imagesy($QR);
        $logo_width = imagesx($logo);
        $logo_height = imagesy($logo);  
        $logo_qr_width = $QR_width / 3;
        $scale = $logo_width / $logo_qr_width;
        $logo_qr_height = $logo_height / $scale;  
        $from_width = ($QR_width - $logo_qr_width) / 2;  
        $from_height = ($QR_height - $logo_qr_height) / 2;
        imagecopyresampled($QR, $logo, $from_width, $from_height, 0, 0, $logo_qr_width, $logo_qr_height, $logo_width, $logo_height);
        imagepng($QR,$last);
        // end of Generate QRcode
        unlink($base);

        if (isset($_GET['down'])||!($path=='/'||$path=='')) {
            // if '?down' or path not null, then return a file
            // 如果指定了下載，或是用的path中的值，則直接輸出文件
            $image_data = fread(fopen($last, 'r'), filesize($last));
            unlink($last);
            return [
                'isBase64Encoded' => true,
                'statusCode' => 200,
                'headers' => [ 'Content-Type' => 'image/png' ],
                'body' => base64_encode($image_data)
            ];
        }

    }

    // start the web html
    // 網頁開始
    @ob_start();
?>
<!DOCTYPE html>
<html>
<head>
    <title>QRcode</title>
    <meta charset=utf-8>
    <meta name="viewport" content="width=device-width,initial-scale=1"/>
</head>
<body>
    <form id="form1" name="form1" method="POST" action="">
        <textarea name="key" rows="5" style="width:100%;height:100%" placeholder="Input value"><?php echo $value;?></textarea><br>
        <input name="Submit1" type="submit" value="Generate QRcode">&nbsp;
        <input name="Submit2" type="submit" value="Download QRcode Directly" onclick="changaction();">
    </form>
<?php
    if ($value != '') echo '    <img src="'. base64EncodeImage($last) .'">
';
?>
    <script>
        function changaction() {
            document.form1.action="?down";
        }
    </script>
</body>
</html>
<?php
    // end the web html
    // 網頁結束
    $html=ob_get_clean();

    $value="";
    unlink($last);

    // return the web html
    // 返回html網頁
    return [
        'isBase64Encoded' => false,
        'statusCode' => 200,
        'headers' => [ 'Content-Type' => 'text/html' ],
        'body' => $html
    ];
}

function base64EncodeImage($image_file)
{
  $base64_image = '';
  $image_info = getimagesize($image_file);
  $image_data = fread(fopen($image_file, 'r'), filesize($image_file));
  //$base64_image = 'data:' . $image_info['mime'] . ';base64,' . chunk_split(base64_encode($image_data));
  $base64_image = 'data:' . $image_info['mime'] . ';base64,' . base64_encode($image_data);
  return $base64_image;
}