<?php

    $N = intval(readline('Valor de N: '));
    
    for ($i = ($N - 1); $i >= 1; $i--) {    
        if( sqrt($i) === floor(sqrt($i)) ){
            echo "Maior quadrado antecessor -> $i\n";
            break;
        }
    }
    
    
    
    
    

?>