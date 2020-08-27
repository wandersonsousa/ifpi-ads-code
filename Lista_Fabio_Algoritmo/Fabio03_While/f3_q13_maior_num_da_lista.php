<?php

#Leia N e uma lista de N números e escreva o maior número da lista.


$N = intval(readline('Valor de N: '));
$maior = 0;

for ($i=0; $i < $N; $i++) { 
    $numeroAtual = intval(readline('Valor: '));
    if($i == 0) $maior = $numeroAtual;
    
    if( $numeroAtual > $N )$maior = $numeroAtual;
}


echo "Maior valor digitado -> $maior\n";







?>