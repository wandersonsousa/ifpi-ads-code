<?php
namespace JWT;
require_once 'jwt.php';

$token = \JWT\generate();

$decoded_token = decode_token($token);

print_r($decoded_token);




function decode_token($token)
{
    $data = [];
    $res = explode('.', $token);
    $data['header'] = json_decode(base64_decode($res[0]));
    $data['payload'] = json_decode(base64_decode($res[1]));

    return $data;
}
