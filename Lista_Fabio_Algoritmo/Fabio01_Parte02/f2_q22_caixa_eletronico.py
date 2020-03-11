#Um algoritmo para gerenciar os saques de um caixa eletrônico deve possuir algum mecanismo para decidir o numero de notas de cada valor que deve ser disponibilizado para o cliente que realizou o saque. Um possível critério seria o da "distribuição ótima" no sentido de que as notas de menor valor disponíveis fossem distribuídas em número mínimo possível. Por exemplo, se a maquina só dispõe de notas de R$ 50, de R$ 10, de R$ 5 e de R$ 1, para uma quantia solicitada de R$ 87, o algoritmo deveria indicar uma nota de R$ 50, três notas de R$ 10, uma nota de R$ 5 e duas notas de R$ 1. Escreva um algoritmo que receba o valor da quantia solicitada e retorne a distribuição das notas de acordo com o critério da distribuição ótima.

#Entrada
quantia_solicitada = int( input("Quantia a retirar: ") )

#Processamento
notas_cinquenta = quantia_solicitada // 50
notas_dez = (quantia_solicitada % 50) // 10
notas_cinco = ( (quantia_solicitada % 50) % 10 ) // 5
notas_um = ((quantia_solicitada % 50) % 10 ) % 5 

#Saida
print("\nDistribuição das notas de 50, 10, 5, e 1 respectivamente >>>>")
print(notas_cinquenta, notas_dez, notas_cinco, notas_um)