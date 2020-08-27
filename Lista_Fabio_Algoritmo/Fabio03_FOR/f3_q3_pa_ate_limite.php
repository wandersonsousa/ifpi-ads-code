<?php
#Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão Aritmética que tem por valor inicial A0 e razão R.

$A0 = intval(readline('Digite o valor inicial da PA: '));
$R = intval(readline('Digite a razão da PA: '));
$limite = intval(readline('Digite o limite: '));

function pegarValorDePA($a1, $r, $n ){
    return $a1 + ($n-1) * $r;
}

for ($i=1; $i <= $limite; $i++) { 
    echo "valor de posição $i equivale à: ". pegarValorDePa($A0, $R, $i) . "\n";
}

?>