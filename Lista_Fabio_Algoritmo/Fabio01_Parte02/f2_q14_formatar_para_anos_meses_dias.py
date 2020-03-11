#Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

#entrada
valor_idade_em_dias = int( input("Digite a idade total em dias: ") )

#processamento
valor_parcial_anos = valor_idade_em_dias // 365
resto_de_anos = valor_idade_em_dias % 365

valor_parcial_meses = resto_de_anos // 30
resto_de_meses = resto_de_anos % 30

valor_parcial_dias = resto_de_meses

print(f"{valor_parcial_anos} anos {valor_parcial_meses} meses  e {valor_parcial_dias} dias")

#saida
