#Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele corresponde.

#entrada
valor_total_min = int(input("Digite o total de minutos: "))

#processamento
valor_parcial_dias = valor_total_min // 1440
resto_de_dias = valor_total_min % 1440

valor_parcial_hrs = resto_de_dias // 60
resto_de_hrs = resto_de_dias % 60

valor_parcial_min = resto_de_hrs

#saida
print(f"{valor_parcial_dias} dias {valor_parcial_hrs} horas e {valor_parcial_min} minutos.")