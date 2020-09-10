<?php

require_once("PHPMailer/PHPMailer.php");
require_once("PHPMailer/SMTP.php");
require_once("PHPMailer/Exception.php");
use PHPMailer\PHPMailer;

# Mailbox related information for sending mail, third party SMTP service, taking   mailbox as an example. 發送郵件使用的電子信箱相關訊息，第三方 SMTP 服務,以 電子信箱爲例
const mail_host="smtp.qq.com";         # SMTP server. SMTP服務器
const mail_user="XXXXXXXXX@qq.com";    # username. 用戶名
const mail_pass="****************";    # The password of the SMTP service. If you use   mailbox, you need to use the generated authorization code. SMTP服務的密碼，如果使用 電子信箱，需使用生成的授權碼
const mail_port=465;                   # SMTP service port. SMTP服務端口

function sendEmail($from,$to,$title,$content){
    $mail = new PHPMailer\PHPMailer();
    //Whether to enable SMTP debug for debugging. It is recommended to open in the development environment and comment out in the production environment. 
    //是否啓用smtp的debug進行調試，開發環境建議開啓，生産環境注釋掉即可
    $mail->SMTPDebug = 2;
    //Send mail using SMTP authentication. 使用smtp鑒權方式發送郵件
    $mail->isSMTP();
    $mail->SMTPAuth=true;
    //The address of Mailbox server. 電子信箱服務器網址
    $mail->Host = mail_host;
    //Setting the login authentication using ssl encryption. 設置使用ssl加密方式登入鑒權
    $mail->SMTPSecure = 'ssl';
    //Setting the remote server port number of the smtp server for SSL connection.   設置ssl連接smtp服務器的遠端服務器端口号
    $mail->Port = mail_port;
    $mail->CharSet = 'UTF-8';
    $mail->Username =mail_user;
    //Smtp login password, if you use   mailbox, you need to use the generated authorization code. smtp登入的密碼，如果使用 電子信箱，需使用生成的授權碼
    $mail->Password = mail_pass;
    //Setting the sender's email address. 設置發件人電子信箱網址
    $mail->From = mail_user;
    //Whether the body of the email is html encoded. 郵件正文是否爲html編碼
    $mail->isHTML(true);
    $mail->addAddress($to,'receiver');
    //Setting the email subject. 設置郵件的主題
    $mail->Subject = $title;
    //Editting email body. Setting 'isHTML' to true above, it can be a full html string. 添加郵件正文 上面将isHTML設置成了true，則可以是完整的html字串
    $mail->Body = $content;
    $status = $mail->send();

    if($status) {
        return true;
    }else{
        return false;
    }
}

function main_handler($event, $context) {
    print "start main handler\n";
    if($event->Records and !empty($event->Records)) {
        $cmqMsgStr = $event->Records[0]->CMQ->msgBody;
        $cmqMsg = json_decode($cmqMsgStr, true);
        var_dump($cmqMsg);
        if(sendEmail($cmqMsg['fromAddr'], $cmqMsg['toAddr'], $cmqMsg['title'], $cmqMsg['body'])) {
            return "send email success";
        }
    }
    return "send email fail";
}

?>