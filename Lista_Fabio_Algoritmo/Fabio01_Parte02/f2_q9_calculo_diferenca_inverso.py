#Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.

#entrada
valor = int( input("Número inteiro com 3 dígitos: ") )

#processamento
primeiro_digito = valor // 100
segundo_digito = valor // 10 - primeiro_digito * 10
terceiro_digito = valor - ( primeiro_digito * 100 + segundo_digito * 10)

valor_inverso = str(terceiro_digito) + str(segundo_digito) + str(primeiro_digito)
#saida
print("Diferença:",valor - int(valor_inverso) )