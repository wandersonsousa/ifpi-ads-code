#entrada
nota_1 = int(input("nota 1:"))
nota_2 = int(input("nota 2:"))
nota_3 = int(input("nota 3:"))

peso_nota_1 = int(input("peso nota 1:"))
peso_nota_2 = int(input("peso nota 2:"))
peso_nota_3 = int(input("peso nota 3:"))
#processamento

numerador = nota_1 * peso_nota_1 + nota_2 * peso_nota_2 + nota_3 * peso_nota_3
soma_pesos = peso_nota_1 + peso_nota_2 + peso_nota_3
#saida
print("media ponderada: ", numerador/soma_pesos)