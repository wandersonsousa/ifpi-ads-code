#O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escreva um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

#Entrada
custo_fabrica = int( input("Digite o custo de fábrica: ") )

#Processamento
custo_total = custo_fabrica
custo_total += custo_fabrica * 0.45
custo_total += custo_fabrica * 0.28

custo_consumidor = custo_total

#Saida
print("O custo ao consumidor é:", custo_consumidor)