<?php
#Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...).
$N = intval(readline('Valor de N: '));
$numerosSortidos = [];

for ($i=1; $i <= $N; $i++) {
    $num = intval(readline('Valor: '));
    array_push($numerosSortidos, $num);
}

sort( $numerosSortidos );

foreach ($numerosSortidos as $n) {
    echo "Número $n \n";
}

























?>