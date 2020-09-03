<?php


function rotateWorld( string $str, int $rotationTimes ) : string {
    if( !isValidString( $str ) )throw new Exception("Invalid String", 1);

    $letters = getLettersFrom($str);

    $rotateString = "";

    foreach($letters as $letter){
        $codeOfLetter = ord($letter);
        
        
        $codeOfLetter = handleCode(  $codeOfLetter, $rotationTimes );
        
        $rotateLetter = chr( $codeOfLetter );
        $rotateString .= $rotateLetter;
    }

    return $rotateString;
}


function isValidString( $str ): bool{
    if( intval($str) )return false;
    return true;
}

function getLettersFrom( $str ) : array{
    return str_split( strtolower( trim($str) ) );
}

function handleCode( $codeOfLetter, $rotationTimes ) : int {
    if( $codeOfLetter + $rotationTimes > 122 ){
        return $codeOfLetter = 96 + $rotationTimes;
    } 

    if( $codeOfLetter + $rotationTimes < 97 ){
        return $codeOfLetter = 122 - $rotationTimes;
    }
    
    return $codeOfLetter = $codeOfLetter + $rotationTimes;
}



echo rotateWorld('a', 1) . "\n";




//ansciiAlphabet 97 -> 122