# Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.Escreva na tela qual dos professores tem salário total maior.


def main():
    horas_aula_prof1 = int(input('PF1: Horas aula >> '))
    valor_ha1 = int(input('PF1: Valor por hora aula >> '))

    horas_aula_prof2 = int(input('PF2: Horas aula >> '))
    valor_ha2 = int(input('PF2: Valor por hora aula >> '))

    salario1 = horas_aula_prof1 * valor_ha1
    salario2 = horas_aula_prof2 * valor_ha2
    if( salario1 > salario2 ):
        print('Professor 1 ganha mais')
    elif( salario1 == salario2):
        print('Ganham o mesmo')
    else:
        print('Professor 2 ganha mais')



    
main()