#Escreva um algoritmo que leia os coeficientes a, b, c, d, e e f, calcule e escreva os valores de x e y.

#Entrada
a = int(input("a >> "))
b = int(input("b >> "))
c = int(input("c >> "))
d = int(input("d >> "))
e = int(input("e >> "))
f = int(input("f >> "))

#Processamento
x = ( c * e - b * f ) / (a * e - b * d)
y = (a * f - c * d) / (a * e - b * d)

#Saida
print(f"Esse são os valores de X:{x:.2f} e Y:{y:.2f}")