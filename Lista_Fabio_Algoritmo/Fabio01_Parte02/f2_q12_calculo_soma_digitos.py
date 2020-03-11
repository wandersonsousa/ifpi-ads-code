#entrada
valor = int( input("Número inteiro de 4 dígitos: ") )

#processamento
valor = str(valor)
soma_digitos = 0

for digito in valor:
    soma_digitos += int( digito )

#saida
print( soma_digitos )