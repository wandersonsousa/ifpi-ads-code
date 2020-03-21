# Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais recente.


def main():
    ano1 = int(input('Data1: Ano >> '))
    mes1 = int(input('Data1: Mes >> '))
    dia1 = int(input('Data1: Dia >> '))

    print('')

    ano2 = int(input('Data2: Ano >> '))
    mes2 = int(input('Data2: Mes >> '))
    dia2 = int(input('Data2: Dia >> '))

    print(data_mais_recente(ano1, mes1, dia1, ano2, mes2, dia2))


def data_mais_recente(ano1, mes1, dia1, ano2, mes2, dia2):

    data1_retorno_str = 'Data 1 é a mais recente'
    data2_retorno_str = 'Data 2 é a mais recente'
    iguais_retorno_str = 'As datas são iguais'

    if ano1 == ano2:
        if mes1 == mes2:
            if dia1 == dia2:
                return iguais_retorno_str
            elif dia1 > dia2:
                return data1_retorno_str
            else:
                return data2_retorno_str

        elif mes1 > mes2:
            return data1_retorno_str
        else:
            return data2_retorno_str
    elif ano1 > ano2:
        return data1_retorno_str
    else:
        return data2_retorno_str


main()
