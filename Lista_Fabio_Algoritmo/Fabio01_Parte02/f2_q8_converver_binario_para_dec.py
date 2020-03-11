#Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.

#Entrada
valor_em_binario = input(" Entregue o número de 4 digítos em binário: ")

#Processamento
quarto_digito = int(valor_em_binario[3]) * 1
terceiro_digito = int(valor_em_binario[2]) * 2
segundo_digito = int(valor_em_binario[1]) * 4
primeiro_digito = int(valor_em_binario[0]) * 8

valor_em_decimal = quarto_digito + terceiro_digito + segundo_digito + primeiro_digito

#Saida
print(f"O binário dado equivale em decimal à: { valor_em_decimal }")