#entrada
minutos = int( input("Digite os minutos: ") )

#processamento
resto = minutos % 60
horas = minutos // 60

#saida
print(f"O horário formatado é: {horas} e {resto}")