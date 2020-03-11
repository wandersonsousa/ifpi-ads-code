#Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas frações, escrevendo o resultado em forma de fração.

#Entrada
numerador1 = int( input("Digite o primeiro numerador: ") )
denominador1 = int( input("Digite o primeiro denominador: ") )

numerador2 = int( input("Digite o segundo numerador: ") )
denominador2 = int( input("Digite o segundo denominador: ") )

#Processamento
mult_denominadores = denominador1 * denominador2

multiplicao1 = (mult_denominadores / denominador1 * numerador1)
multiplicao2 = (mult_denominadores / denominador2 * numerador2)

numerador_final = multiplicao1 + multiplicao2
denominador_final = mult_denominadores

print( "{:.0f}/{}".format(numerador_final, denominador_final) )

#Saida