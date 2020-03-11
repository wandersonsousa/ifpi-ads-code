#Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, ponto1 (x1,y1) e ponto2 (x2,y2), escreva a distância entre eles, conforme fórmula abaixo.

#Entrada
x1 = int( input("X1 >> ") )
y1 = int( input("y1 >> ") )

x2 = int( input("x2 >> ") )
y2 = int( input("y2 >> ") )

#Processamento
distancia_pontos = ( (x2 - x1)**2 + (y2-y1) ** 2 ) ** (1/2)

#Saida
print("A distancia entre os pontos equivale a: {:.2f}".format(distancia_pontos))