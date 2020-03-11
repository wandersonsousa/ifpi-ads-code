#Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão do 1o pelo 2o.
#entrada
num_1 = int(input("primeiro numero: "))
num_2 = int(input("segundo numero: "))
#processamento

quociente = num_1 // num_2
resto = num_1 % num_2
#saida
print(f"quociente: {quociente},resto: {resto}")