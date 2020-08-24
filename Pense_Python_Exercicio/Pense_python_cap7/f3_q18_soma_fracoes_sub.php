<?php
#Leia N, calcule e escreva o valor de S


$N = intval(readline('Valor de N: '));
$S = 0;


for ($i=1; $i <= $N; $i++) { 
    if($i === 1)continue;

    $S += $i / ($i - 1);
    echo "$i / ($i - 1) = $S \n ";
}


echo "Valor Final de S => $S \n";