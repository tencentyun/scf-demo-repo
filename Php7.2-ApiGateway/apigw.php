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
        return 'success';
    }
    else {
        return 'event is not come from api gateway';
    }
}

?>