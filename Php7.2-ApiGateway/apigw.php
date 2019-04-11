<?php

function main_handler($event, $context) {
    print "start main handler\n";
    $content = "API GW Test Success";

    //构造API网关返回值
    $rep = array(
    "isBase64Encoded" => false,
    "statusCode"=> 200,
    "headers"=> array(
        "Content-Type"=>"text/html"
        ),
    "body"=> $content,
    );
    // $rep = json_encode($rep.true)
    return $rep;
}

?>