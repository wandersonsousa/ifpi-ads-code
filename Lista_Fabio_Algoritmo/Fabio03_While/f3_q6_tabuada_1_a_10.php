<?php
#Escreva a tabuada dos números de 1 a 10.

function tabuadaDe( $tipoTabuada ){
    switch ($tipoTabuada) {
        case 'multiplicacao':
            for ($i=1; $i <= 10; $i++) { 
                tabuadaMultDe($i);
                echo "\n";
            }
            break;
        case 'divisao':
            for ($i=1; $i <= 10; $i++) { 
                tabuadaDivDe($i);
                echo "\n";
            }
            break;
        case 'soma':
            for ($i=1; $i <= 10; $i++) { 
                tabuadaSomaDe($i);
                echo "\n";
            }
            break;
        case 'subtracao':
            for ($i=1; $i <= 10; $i++) { 
                tabuadaSubtracaoDe($i);
                echo "\n";
            }
            break;
        default:
            # code...
            break;
    }
}


function tabuadaMultDe( $n ){
    $i = 1;
    while($i <= 10){
        echo "$i x $n = " . ($n * $i) . "\n";
        $i++;
    }
}
function tabuadaDivDe( $n ){
    $i = 1;
    while ($i <= 10) {
        echo "$i / $n = " . number_format( ($n / $i), 2 ) . "\n";
        $i++;
    }
}
function tabuadaSomaDe( $n ){
    $i = 1;
    while ($i <= 10) {
        echo "$i + $n = " . ($n + $i) . "\n";
        $i++;
    }
}
function tabuadaSubtracaoDe( $n ){
    $i=1;
    while ( $i <= 10) {
        echo "$i - $n = " . ($i - $n) . "\n";
        $i++;
    }
}

$on = true;

while ($on){
    showMenu();
    $escolha = pegarEscolhaDeTabuada();
    menuController($escolha);
}



function showMenu(){
    echo "--------------------_ Menu _-------------------\n";
    echo "[1]Adição\n";
    echo "[2]Subtração\n";
    echo "[3]Multiplicação\n";
    echo "[4]Divisão\n";
    echo "[0]SAIR\n";
    echo "[5]LIMPAR TELA\n";

    echo "\n\n";
}

function pegarEscolhaDeTabuada(){
    return intval(readline('Escolha: '));

}

function menuController($escolha){
    switch ($escolha) {
        case 1:
            clearScreen();
            echo "Tabuada De Adição\n";
            tabuadaDe('soma');
            break;
        case 2:
            clearScreen();
            echo "Tabuada de Subtração\n";
            tabuadaDe('subtracao');
            break;
        case 3:
            clearScreen();
            echo "Tabuada de Multiplicação\n\n";
            tabuadaDe('multiplicacao');
            break;
        case 4:
            clearScreen();
            echo "Tabuada de Divisão\n";
            tabuadaDe('divisao');
            break;
        case 5:
            clearScreen();
            break;
        case 0:
            breakApp();
            break;
        default:
            clearScreen();
            echo "Opção Inválida\n";
            break;
    }
}
function breakApp(){
    global $on;
    $on = false;
}
function clearScreen(){
    if(PHP_OS === 'Linux')system('clear');
    else if(PHP_OS === 'Windows')system('cls');
}

?>