<?php
#Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.

$N = intval(readline('Valor de N: '));
$soma = 0;

for ($i=0; $i <= $N; $i++) { 
    $soma += $i;
}

echo "Média : ". ($soma / ($N + 1) ) . "\n";


?>