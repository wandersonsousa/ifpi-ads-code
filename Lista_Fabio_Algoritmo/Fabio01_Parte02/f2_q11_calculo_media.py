#Leia 3 números, calcule e escreva a média dos números.

#entrada
valor_1 = int(input("primeiro valor: "))
valor_2 = int(input("segundo valor: "))
valor_3 = int(input("terceiro valor: "))

#processamento
media_valores = (valor_1 + valor_2 + valor_3) / 3

#saida
print( 'A média é: {:.2f}'.format(media_valores) )
