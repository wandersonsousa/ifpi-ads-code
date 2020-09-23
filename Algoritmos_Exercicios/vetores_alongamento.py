#- Pergunte ao Usuário quantos números ele pretende digitar; 
#- Crie um vetor do tamanho do valor informado, com valor padrão -1
#- Em seguida receba cada um dos números e armazene sequencialmente em vetor criado
#- Após receber, conte quantos números são Pares, Ímpares, Negativos e Positivos e apresente ao usuário

#- Substitua todos os números em posições para o Dobro do valor atual se ela for Positiva ou por sua metade se ela for Negativa
#- Mostre novamente Qtd de Pares, Ímpares, Negativos e Positivos
#- Apresente a média dos Valores, após a transformação
#- Experimente criar Funções para suas operações acima. Vetores podem ser enviados para .. e recebidos de funções


howManyNumbers = int(input('Quantos valores pretende digitar: '))
array = []
for number in range(0, howManyNumbers):
    n = int(input('Digite um número: '))
    array.append( n )



def isPair( n ):
    return n % 2 == 0
def isPositive(n):
    return n >= 0


def parseNumbersInArray( array ):
    for i in range(len(array)):
        if( isPositive(array[i]) ):
            array[i] = array[i] * 2
        else:
            array[i] = array[i] / 2
    return array

def showTypeNumbers( array ):
    for n in array:
        print('-' * 20)
        if( isPair( n ) ):
            print('{} é par'.format(n))
        else:
            print('{} é ímpar'.format(n))

        if( isPositive(n) ):
            print('{} é positivo'.format(n))
        else:
            print('{} é negativo'.format(n))

def mediaNumbersIn( array ):
    media = 0
    for n in array:
        media += n
    return media / len(array)



showTypeNumbers( array )

array = parseNumbersInArray(array)

print('-+' * 40)

showTypeNumbers( array )

print('-+' * 40)

print('média ->', mediaNumbersIn(array) )