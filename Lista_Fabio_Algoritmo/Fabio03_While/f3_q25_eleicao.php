<?php


#Em uma eleição presidencial existem 3 (três) candidatos. Os votos são informados através de códigos.Os dados utilizados para a contagem dos votos obedecem à seguinte codificação: · 1, 2, 3 = voto para os respectivos candidatos; · 9 = voto nulo; · 0 = voto em branco; Escreva um algoritmo que leia o código votado por N eleitores. Ao final, calcule e escreva: a) total de votos para cada candidato; b) total de votos nulos; c) total de votos em branco; d) quem venceu a eleição.

$N = intval( readline('Digite N : ') );

$i = 1;

$candidato1 = $candidato2 = $candidato3 = $votoNulo = $votoBranco =  0;
while ( $i <= $N ){
    $voto = intval( readline('Vote : ') );
    if( $voto === 1 ){
        ++$candidato1;
    }elseif( $voto === 2 ){
        ++$candidato2;
    }elseif( $voto === 3 ){
        ++$candidato3;
    }elseif( $voto === 9){
        ++$votoNulo;
    }elseif($voto === 0){
        ++$votoBranco;
    }
    $i++;
}

echo "-------------------------- RESULTADO --------------------------- \n";
echo "Votos para candidato 1 = $candidato1 \n";
echo "Votos para candidato 2 = $candidato2 \n";
echo "Votos para candidato 3 = $candidato3 \n";
echo "Votos Nulos = $votoNulo \n";
echo "Votos em Branco = $votoBranco \n"; 