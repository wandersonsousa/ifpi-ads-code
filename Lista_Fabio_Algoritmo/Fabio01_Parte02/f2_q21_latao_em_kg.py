#Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo que calcule a quantidade de cada um desses componentes para se obter certa quantidade de latão (em kg), informada pelo usuário.

#Entrada
qntd_latao = int( input("Digite qual o peso do latão: ") )

#Processamento
qntd_cobre = qntd_latao * 0.7
qntd_zinco = qntd_latao * 0.3

#Saida
print(f"Você vai precisar de {qntd_cobre:.2f} de cobre e {qntd_zinco:.2f} de zinco")