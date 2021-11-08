<?php

namespace JWT;

function generateToken()
{
    //Application Key
    $key = generateKey();

    //Header Token
    $header = generateHeader();

    //Payload - Content
    $payload = generatePayload();

    //JSON
    $tokenInfoAsJson = encodeTokenInformationToJson($header, $payload);

    //Base 64
    $tokenInfoAsBase64 = encodeJsonTokenInformationToBase64( $tokenInfoAsJson['header'], $tokenInfoAsJson['payload'] );

    //Sign
    $sign = generateTokenSign($header, $payload, $key);

    //Token
    return $header . '.' . $payload . '.' . $sign;
}



function generateTokenSign($header, $payload, $key){
    $sign = hash_hmac('sha256', $header . "." . $payload, $key, true);
    return base64_encode($sign);
}


function encodeTokenInformationToJson($header, $payload){
    return [
        'header' => json_encode($header),
        'payload' =>  json_encode($payload)
    ];
}
function encodeJsonTokenInformationToBase64($header, $payload){
    return [
        'header' => base64_encode($header),
        'payload' =>  base64_encode($payload)
    ];
}


function generateKey(){
    return 'hOLLY sHIT';
}
function generateHeader(){
    return  [
        'typ' => 'JWT',
        'alg' => 'HS256'
    ];
}
function generatePayload(){
    return [
        'exp' => (new \DateTime("now"))->getTimestamp(),
        'uid' => 1,
        'email' => 'email@email.com',
    ];
}