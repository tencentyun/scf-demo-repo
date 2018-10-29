<?php

require_once("PHPMailer/PHPMailer.php");
require_once("PHPMailer/SMTP.php");
require_once("PHPMailer/Exception.php");
use PHPMailer\PHPMailer;

# 发送邮件使用的邮箱相关信息，第三方 SMTP 服务,以QQ邮箱为例
const mail_host="smtp.qq.com";         #SMTP服务器
const mail_user="XXXXXXXXX@qq.com";    #用户名
const mail_pass="****************";    #SMTP服务的口令，如果使用QQ邮箱，需使用生成的授权码
const mail_port=465;                   #SMTP服务端口

function sendEmail($from,$to,$title,$content){
    $mail = new PHPMailer\PHPMailer();
    //是否启用smtp的debug进行调试，开发环境建议开启，生产环境注释掉即可
    $mail->SMTPDebug = 2;
    //使用smtp鉴权方式发送邮件
    $mail->isSMTP();
    $mail->SMTPAuth=true;
    //邮箱服务器地址
    $mail->Host = mail_host;
    //设置使用ssl加密方式登录鉴权
    $mail->SMTPSecure = 'ssl';
    //设置ssl连接smtp服务器的远程服务器端口号
    $mail->Port = mail_port;
    $mail->CharSet = 'UTF-8';
    $mail->Username =mail_user;
    //smtp登录的密码，如果使用QQ邮箱，需使用生成的授权码
    $mail->Password = mail_pass;
    //设置发件人邮箱地址
    $mail->From = mail_user;
    //邮件正文是否为html编码
    $mail->isHTML(true);
    $mail->addAddress($to,'receiver');
    //设置邮件的主题
    $mail->Subject = $title;
    //添加邮件正文 上面将isHTML设置成了true，则可以是完整的html字符串
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