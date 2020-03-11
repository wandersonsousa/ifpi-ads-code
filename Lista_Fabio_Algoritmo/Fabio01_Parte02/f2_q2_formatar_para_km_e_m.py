#Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.

#entrada
valor_em_m = int(input("Digite valor em metros: "))

#processamento
valor_parcial_km = valor_em_m // 1000
valor_parcial_m = valor_em_m % 1000

#saida
print(f"{valor_parcial_km}km e {valor_parcial_m}m")