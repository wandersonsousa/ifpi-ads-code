<?php
#Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão Geométrica que tem por valor inicial A0 e razão R.

$A0 = intval(readline('Digite o valor inicial da PG: '));
$R = intval(readline('Digite a razão da PG: '));
$limite = intval(readline('Digite o limite: '));

function pegarValorDePG($a1, $r, $n ){
    return $a1 * $r ** ( $n - 1 );
}

for ($i=1; $i <= $limite; $i++) { 
    echo "valor de posição $i equivale à: ". pegarValorDePG($A0, $R, $i) . "\n";
}