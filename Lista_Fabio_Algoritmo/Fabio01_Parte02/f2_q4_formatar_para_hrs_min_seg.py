#Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.

#entrada
valor_total_seg = int(input("Digite o total de segundos: "))

#processamento
valor_parcial_hrs = valor_total_seg // 3600
resto_de_hrs = valor_total_seg % 3600

valor_parcial_min = resto_de_hrs // 60
resto_de_min = valor_total_seg % 3600

valor_parcial_seg = resto_de_min

#saida
print(f"{valor_parcial_hrs} horas {valor_parcial_min} minutos e {valor_parcial_seg} segundos")