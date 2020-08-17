<?php

#Leia LimiteSuperior e LimiteInferior e escreva todos os números pares entre os limites lidos.

$limiteInferior = intval(readline('Valor do limite inferior: '));
$limiteSuperior = intval(readline('Valor do limite superior: '));



for ($i=$limiteInferior; $i <= $limiteSuperior; $i++) { 
    if($i % 2 === 0){   
        echo "Valor Par : $i\n";
    }
    
}











?>