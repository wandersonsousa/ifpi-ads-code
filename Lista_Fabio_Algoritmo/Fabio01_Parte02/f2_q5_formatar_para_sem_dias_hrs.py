#Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele corresponde.

#entrada
valor_total_hrs = int(input("Digite o total de horas: "))

#processamento
valor_parcial_sem = valor_total_hrs // 168
resto_de_sem = valor_total_hrs % 168

valor_parcial_dias = resto_de_sem // 24
resto_de_dias = valor_total_hrs % 24

valor_parcial_hrs = resto_de_dias

#saida
print(f"{valor_parcial_sem} semanas {valor_parcial_dias} dias e {valor_parcial_hrs} horas")