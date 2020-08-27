<?php

#Uma determinada empresa armazena para cada funcionário uma ficha contendo o código, o número de horas trabalhadas e o seu no de dependentes.
#Considerando que a empresa paga R$ 12,00 por hora e R$ 40,00 por dependentes e que sobre o salário são feitos descontos de 8,5% para o INSS e 5% para IR. Escreva um algoritmo que leia o código, número de horas trabalhadas e número de dependentes de N funcionários. Após a leitura de cada ficha, escreva os valores descontados para cada imposto e o salário líquido do funcionário.


$N = intval(readline('Valor de N: '));
$funcionarios = [];

echo "\n \n \n";
for ($i=1; $i <= $N; $i++) {
    echo "---------------------------\n \n";
    echo "Ficha de número $i \n ";
    
    $nome = strval( readline('Nome: ') );
    $codigo = intval( readline('Código : ') );
    $horasTrabalhadas =  floatval( readline('Horas trabalhadas : ') );
    $numDependentes =  floatval( readline('N° de dependentes : ') );

    $salarioBruto = ($horasTrabalhadas * 12) + (40 * $numDependentes);

    $descontadoParaINSS = $salarioBruto * 0.085;
    $descontadoParaIR = $salarioBruto * 0.05;

    $salarioLiquido = $salarioBruto - $descontadoParaINSS - $descontadoParaIR;

    array_push( $funcionarios, [
        'nome'=>$nome,
        'codigo'=>$codigo,
        'horasTrabalhadas'=>$horasTrabalhadas,
        'numDependentes'=>$numDependentes,
        'salario'=>$salarioLiquido,
        'descontadoINSS'=>$descontadoParaINSS,
        'descontadoIR'=>$descontadoParaIR
    ]);

    echo "\n \n";
}



foreach( $funcionarios as $funcionario ){
    echo "----------------------------------- \n";
    echo "Funcionário : ". $funcionario['nome'] . "\n";
    echo "Código : ". $funcionario['codigo'] . "\n";
    echo "Salário Liquído : ". $funcionario['salario'] . "\n";
    echo "Descontado INSS : ". $funcionario['descontadoINSS'] . "\n";
    echo "Descontado IR : ". $funcionario['descontadoIR'] . "\n";
}