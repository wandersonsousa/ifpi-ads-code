<?php
#Leia N, calcule e escreva o valor de S


$N = intval(readline('Valor de N: '));
$S = 0;
$i=1;

while ($i <= $N) { 
    $S += 1 / $i;
    $i++;
}


echo "Valor Final de S => $S \n";