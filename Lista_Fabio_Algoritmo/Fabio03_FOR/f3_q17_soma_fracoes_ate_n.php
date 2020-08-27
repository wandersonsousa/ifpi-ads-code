<?php
#Leia N, calcule e escreva o valor de S


$N = intval(readline('Valor de N: '));
$S = 0;


for ($i=1; $i <= $N; $i++) { 
    $S += 1 / $i;
}


echo "Valor Final de S => $S \n";