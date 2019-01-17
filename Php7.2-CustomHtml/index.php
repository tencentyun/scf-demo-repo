<?php

$gl = 1;

function renderTpl($tpl,$variables){
    foreach ($variables as $key => $value) {
        $regex = '/\$\{'.$key.'\}/';
        $tpl = preg_replace($regex,$value,$tpl);
    }
    echo $tpl;
    return $tpl;
}

function main_handler($event, $context) {
    $filePath = dirname(__FILE__)."/index.html";
    $fileHandle = fopen($filePath, "a+");
    $html = fread($fileHandle, filesize($filePath));

    $html = renderTpl($html,[
        "master"=> '深圳腾讯科技公司', // 您的名称
        "centralCouplet"=> '年年有余', // 横批
        "upCouplet"=> '千年迎新春', // 上联
        "downCouplet"=> '瑞雪兆丰年' // 下联
    ]);

    fclose($fileHandle);

    return  [
        "isBase64Encoded"=> false,
        "statusCode"=> 200,
        "headers"=> [ 'Content-Type'=> 'text/html' ],
        "body"=> $html
    ];
}
?>
