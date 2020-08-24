<?php

# prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e escreva: 
#a) média de salário da população; 
#b) média de número de filhos;
# c) percentual de pessoas com salário de até R$ 1.000,00.


$N = intval(readline('Valor de N: '));
$habitantes = [];

echo "\n \n \n";
$count = 1;
while($count <= $N) {
    echo "---------------------------\n \n";
    echo "Habitante de número $count \n ";
    
    $salario = intval( readline('Salário: ') );
    $numeroDeFilhos = intval( readline('N° de filhos : ') );

    array_push( $habitantes, [
        'salario'=>$salario,
        'numeroDeFilhos'=>$numeroDeFilhos
    ]);

    echo "\n \n";
    $count++;
}



$media_salarial = array_reduce($habitantes, 'somarSalarios') / count($habitantes);
$media_filhos = array_reduce($habitantes, 'somarNumeroFilhos') / count($habitantes);
function somarSalarios($atual, $anterior){
    return $anterior['salario'] + $atual;
}
function somarNumeroFilhos($atual, $anterior){
    return $anterior['numeroDeFilhos'] + $atual;
}


$salariosAcimaDeMil = array_filter($habitantes, 'salarioAcimaMil');
function salarioAcimaMil($habitante){
    return $habitante['salario'] > 1000;
}
$percentualAcimaMil = (count($salariosAcimaDeMil) * 100 ) / count($habitantes);

echo "Média Salarial: $media_salarial\n";
echo "Média no Número de filhos: $media_filhos \n";
echo "Percentual de pessoas com salário de até R$ 1.000,00: $percentualAcimaMil \n";

