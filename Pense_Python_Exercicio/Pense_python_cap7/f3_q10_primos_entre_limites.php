<?php

#Leia LimiteSuperior e LimiteInferior e escreva todos os números primos entre os limites lidos.

$limiteInferior = intval(readline('Valor do limite inferior: '));
$limiteSuperior = intval(readline('Valor do limite superior: '));


echo "\n \n ---------------------------- \n \n";

for ($i=$limiteInferior; $i <= $limiteSuperior; $i++) { 
    if( eh_primo($i) ){
        echo "Número Primo Encontrado : $i\n";
    }    
}



function eh_primo($n){
    if($n === 1)return false;

    for ($i=1; $i <= $n ; $i++) { 
        if($n % $i === 0 && $i !== $n && $i !== 1){
            return false;
        }
    }

    return true;
}








?>