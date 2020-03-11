#Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:

#Entrada
A = int(input("Digite o primeiro valor: "))
B = int(input("Digite o segundo valor: "))
C = int(input("Digite o terceiro valor: "))
#Processamento
R = ( A + B ) ** 2
S = ( B + C ) ** 2

D = (R + S) / 2
#Saida
print("Resultado:", D)