<?php
#Leia N, calcule e escreva o valor de S


$N = intval(readline('Valor de N: '));
$S = 0;
echo "\n";

for ($i=1; $i <= $N; $i++) {
     
    if($i === 1){
        $S = 1 / $i;
        echo "1 / $i = $S\n";
        --$i;
        continue;
    }

    if( eh_par($i) ){
        $S -= ($i - ($i - 1) ) / $i;   
        echo "($i - ($i - 1) ) / $i = $S\n ";
    }else{
        $S += $i / ($i - ($i - 1));
        echo "$i / ($i - ($i - 1) ) = $S\n ";
    }

    echo "\n";
}

function eh_par($n){
    return $n % 2 === 0;
}


echo "Valor Final de S => $S \n";

