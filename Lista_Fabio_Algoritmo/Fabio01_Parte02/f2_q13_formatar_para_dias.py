#Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

#entrada
valor_anos = int( input("Sua idade apenas em anos: ") )
valor_meses = int( input("Sua idade apenas em meses: ") )
valor_dias = int( input("Sua idade apenas em dias: ") )

#processamento

idade_total_dias = valor_anos * 365 + valor_meses * 30 + valor_dias

#saida
print("Idade total em dias:", idade_total_dias)