#Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

#entrada
total_dias = int(input("Digite o total de dias: "))

#processamento
valor_parcial_semanas = total_dias // 7
valor_parcial_dias = total_dias % 7

#saida
print(f"{valor_parcial_semanas} semanas e {valor_parcial_dias} dias")