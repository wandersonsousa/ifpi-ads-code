<?php


function rotateWorld( string $str, int $rotationTimes ) : string {
    define('Alphabet', range('a', 'z') );

    $letters = getLettersFrom($str);
    $rotateString = "";

    foreach($letters as $letter){
        if( ctype_alpha($letter) ){
            $codeOfLetter = array_search($letter, Alphabet);
            if( $codeOfLetter + $rotationTimes >  25){
                $codeOfLetter = ( $codeOfLetter + $rotationTimes ) - 26;                 
            }
            elseif( $codeOfLetter + $rotationTimes < 0){
                $codeOfLetter = ( $codeOfLetter + 26 ) + $rotationTimes;
            }          
            else{
                $codeOfLetter += $rotationTimes;
            }
        }else {
            $rotateString .= $letter;
            continue;
        }
        
        $rotateLetter = Alphabet[ $codeOfLetter ];
        $rotateString .= $rotateLetter;
    }

    return $rotateString;
}






function getLettersFrom( $str ) : array{
    return str_split( strtolower( trim($str) ) );
}


echo rotateWorld('a', -1 ) . "\n";




//ansciiAlphabet 97 -> 122