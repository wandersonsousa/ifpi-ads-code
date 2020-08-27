<?php
# Leia N e escreva todos os números inteiros pares de 1 a N.s
$N = intval(readline('Digite N: '));

$i = 0;
while($i <= $N){
    $i++;
    if($i % 2 === 0)echo "valor par => $i \n";
}


?>