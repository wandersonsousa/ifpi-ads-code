#Leia um número inteiro (3 dígitos), calcule e escreva a soma entre o número e seu inverso.

#entrada
valor = int( input("Número com 3 dígitos: ") )

#processamento
valor_inverso = str(valor)[::-1] 
soma_valores = valor + int( valor_inverso)

#saida
print( soma_valores )