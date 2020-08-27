<?php

#Um fazendeiro possui fichas de controle sobre sua boiada. Cada ficha contém numero de identificação, nome e peso (em kg) do boi. Escreva um algoritmo que leia os dados de N fichas e ao final, escreva o numero de identificação e o peso do boi mais magro e do boi mais gordo.


$N = intval(readline('Valor de N: '));
$maisMagro = $maisGordo = $identificacaoGordo = $identificacaoMagro = null;

echo "\n \n \n";
for ($i=1; $i <= $N; $i++) { 
    echo "---------------------------\n \n";
    echo "Ficha de número $i \n ";
    
    $nome = strval( readline('Nome: ') );
    $numeroIdentificacao = intval( readline('Número de identificação : ') );
    $peso =  floatval( readline('Peso: ') );

    echo "\n \n";
    
    if($i == 1){
        $identificacaoGordo = $identificacaoMagro = $nome;
        $maisGordo = $maisMagro = $peso;
    }

    if($peso > $maisGordo){
        $maisGordo = $peso;
        $identificacaoGordo = $nome;
    }
    if($peso < $maisMagro){
        $maisMagro = $peso;
        $identificacaoMagro = $nome;
    }
}

echo "Boi mais gordo => $identificacaoGordo, peso => $maisGordo \n";
echo "Boi mais magro => $identificacaoMagro, peso => $maisMagro \n";