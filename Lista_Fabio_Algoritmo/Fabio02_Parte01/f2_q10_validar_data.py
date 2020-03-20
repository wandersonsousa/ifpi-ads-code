# Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.


def main():
    dia = input('Dia >> ')
    mes = input('Mes >> ')
    ano = input('Ano >> ')

    print(data_eh_valida(dia, mes, ano))


def data_eh_valida(d, m, a):
    d = int(d)
    m = int(m)
    a = int(a)

    if(d <= 30 and d >= 1):
        if(m < 12 and m >= 1):
            if(a > 0):
                return f'{d}/{m}/{a} é válido'
    else:
        return 'Data inválida'


main()
