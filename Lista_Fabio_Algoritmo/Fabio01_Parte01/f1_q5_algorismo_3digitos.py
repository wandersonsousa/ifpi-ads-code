#entrada
numero = int( input("Digite o algorismo de 3 digitos: ") )

#processamento
numero_1 = numero // 100
numero_2 = numero - numero_1 * 100
numero_3 = numero_2 // 10
numero_4 = numero_2 - numero_3 * 10 

#saida
print("A soma dos números: ", numero_1+numero_3+numero_4)