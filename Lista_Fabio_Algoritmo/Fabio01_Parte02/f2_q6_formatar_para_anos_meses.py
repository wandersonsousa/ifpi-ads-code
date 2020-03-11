#Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.

#entrada
valor_total_meses = int(input("Digite o total de meses: "))

#processamento
valor_parcial_anos = valor_total_meses // 12
resto_de_anos = valor_total_meses % 12

valor_parcial_meses = resto_de_anos

#saida
print(f"{valor_parcial_anos} anos e {valor_parcial_meses} meses")