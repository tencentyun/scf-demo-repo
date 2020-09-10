<?php

require_once("PHPMailer/PHPMailer.php");
require_once("PHPMailer/SMTP.php");
require_once("PHPMailer/Exception.php");
use PHPMailer\PHPMailer;

# The user's mail information, here we use qq mail as an example
# 發送郵件使用的電子信箱相關訊息，第三方 SMTP 服務,以 電子信箱爲例
const mail_host="smtp.qq.com";         #SMTPhost
const mail_user="XXXXXXXXX@qq.com";    #user's name
const mail_pass="****************";    #SMTP service password，if you use qq mail, please fill in the authentication code
const mail_port=465;                   #SMTP port

# The test url
# 要撥測的URL網址
$test_url_list = array(
    "http://www.baidu.com",
    "http://www.qq.com",
    "http://wrong.taifucloud.com",
    "http://unkownurl.com"
);

# The email to receive notify
# 接收報警的電子信箱網址
$email_notify_list = array(
    "XXXXXXXXX@qq.com"
);

function sendEmail($to,$title,$content){
    $mail = new PHPMailer\PHPMailer();
    // we suggest you use smtp debug for debugging in development environment
    //是否啓用smtp的debug進行調試，開發環境建議開啓，生産環境注釋掉即可
    $mail->SMTPDebug = 2;
    // Use smtp authentication to send email
    // 使用smtp鑒權方式發送郵件
    $mail->isSMTP();
    $mail->SMTPAuth=true;
    // email host
    //電子信箱服務器網址
    $mail->Host = mail_host;
    //Use ssl for log in authentication
    //設置使用ssl加密方式登入鑒權
    $mail->SMTPSecure = 'ssl';
    //Setting remote smtp host port for ssl connection
    //設置ssl連接smtp服務器的遠端服務器端口号
    $mail->Port = mail_port;
    $mail->CharSet = 'UTF-8';
    $mail->Username =mail_user;
    //smtp password, if you use qq mail, fill in the generated authentication code
    //smtp登入的密碼，如果使用 電子信箱，需使用生成的授權碼
    $mail->Password = mail_pass;
    //The sender's email address
    //設置發件人電子信箱網址
    $mail->From = mail_user;
    //Check whether the mail content is html format
    //郵件正文是否爲html編碼
    $mail->isHTML(true);
    $mail->addAddress($to,'receiver');
    //Email subject
    //設置郵件的主題
    $mail->Subject = $title;
    //Add mail content
    //添加郵件正文 上方将isHTML設置成了true，則可以是完整的html字串
    $mail->Body = $content;
    $status = $mail->send();

    if($status) {
        return true;
    }else{
        return false;
    }
}

function test_url($test_url_list) {
    $curl = curl_init();
    $timeout = 3;
    $errorinfo = array();
    foreach ($test_url_list as $test_url) {
        print "Testing $test_url ";
        // Setting url
        // 設置url路徑
        curl_setopt($curl, CURLOPT_URL, $test_url);
        // Return the curl_exec() message in file stream format
        // 将 curl_exec()獲取的訊息以文件流的形式返回，而不是直接輸出。
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true) ;
        // Return thre data when start CURLOPT_RETURNTRANSFER
        // 在啓用 CURLOPT_RETURNTRANSFER 時候将獲取數據返回
        curl_setopt($curl, CURLOPT_BINARYTRANSFER, true) ;
        // Set timeout
        // 設置超時時間
        curl_setopt ($curl, CURLOPT_CONNECTTIMEOUT, $timeout);
        // Retrive the head request information by CURLINFO_HEADER_OUT
        // CURLINFO_HEADER_OUT選項可以拿到請求頭訊息
        curl_setopt($curl, CURLINFO_HEADER_OUT, true);
        // Execution
        // 執行
        $data = curl_exec($curl);
        $info = curl_getinfo($curl);
        $status_code = $info['http_code'];
        print "return $status_code\n";
        if ($status_code == 0 || $status_code >= 400) {
            print "response status code fail: $status_code\n";
            $errorinfo[] = "Access $test_url fail, status code: $status_code";
        }
    }
    // Disconnection
    curl_close($curl);
    if (!empty($errorinfo)) {
        $body = join("<br />", $errorinfo);
        $subject = "Please note: PlayCheck Error";
        global $email_notify_list;
        foreach ($email_notify_list as $to_addr) {
            sendEmail($to_addr, $subject, $body);
        }
    }
}

function main_handler($event, $context) {
    global $test_url_list;
    test_url($test_url_list);
}

?>