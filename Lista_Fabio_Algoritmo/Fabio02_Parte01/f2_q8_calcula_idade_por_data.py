# Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule e escreva sua idade exata (em anos).


def main():
    ano_atual = int(input('Digite o ano atual >> '))
    mes_atual = int(input('Digite o mes atual >> '))
    dia_atual = int(input('Digite o dia atual >> '))

    ano_nasc = int(input('Digite o ano que nasceu >> '))
    mes_nasc = int(input('Digite o mes que nasceu >> '))
    dia_nasc = int(input('Digite o dia que nasceu >> '))

    calcular_idade_atual(ano_atual, mes_atual, dia_atual,
                         ano_nasc, mes_nasc, dia_nasc)


def calcular_idade_atual(ano_atual, mes_atual, dia_atual, ano_nasc, mes_nasc, dia_nasc):

    meses_totais_atuais = ano_atual * 12 + mes_atual
    meses_nasc_total = ano_nasc * 12 + mes_nasc

    idade_ano = (meses_totais_atuais - meses_nasc_total) // 12

    print(idade_ano)



main()
