#Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número de anos que ele fuma, o no de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).

#Entrada
anos_fumando = int( input("Quantidade de anos como fumante: ") )
cigarros_dia = int( input("Quantidade de cigarros fumados por dia: ") )
preco_da_carteira = int( input("Preco da carteira: ") )

#Processamento
qntd_carteira_dia = cigarros_dia / 20
total_carteiras = (qntd_carteira_dia * 365) * anos_fumando

#Saida
print("Dinheiro total gasto:", total_carteiras * preco_da_carteira)