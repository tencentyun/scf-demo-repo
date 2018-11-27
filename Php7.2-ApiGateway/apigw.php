<?php

function main_handler($event, $context) {
    print "start main handler\n";
    if($event->requestContext) {
        $req = $event->requestContext;
        print "Process request:\n";
        print "method: $event->httpMethod\n";
        print "path: $event->path\n";
        print "match method: $req->httpMethod\n";
        print "match path: $req->path\n";
        print "sourceIp: $req->sourceIp";
        $content='API GW Test';
    }
    else {
        $content = 'event is not come from api gateway';
    }

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