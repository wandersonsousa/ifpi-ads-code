#entrada
horas = int( input("Digite a hora: ") )
minutos = int( input("Digite os minutos: ") )

#processamento
horas_em_minutos = horas * 60
minutos_total = horas_em_minutos + minutos

#saida
print(f"Em minutos: {minutos_total}")
