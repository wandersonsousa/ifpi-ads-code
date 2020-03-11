#Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.

#entrada

numero_1 = int( input("Digite o primeiro numero: ") )
numero_2 = int( input("Digite o segundo numero: ") )

#processamento

soma = numero_1 + numero_2
diferenca = numero_1 - numero_2
divisao = soma / diferenca

#saida

print("Resultado: ", divisao)
