# Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 variáveis inteiras:hora e minuto). Calcule e escreva a duração do jogo (horas e minutos), sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia seguinte.


def main():
    inicio_hora = int(input("digite o hora do inicio do jogo >> "))
    inicio_minuto = int(input("digite o minuto do inicio do jogo >> "))

    fim_hora = int(input("digite o hora de saida do jogo >> "))
    fim_minuto = int(input("digite o minuto de saida do jogo >> "))

    calcular_duracao(inicio_hora, inicio_minuto, fim_hora, fim_minuto)


def entrada_nao_valida(horas, minutos):
    return (horas > 24) or (horas < 1) or (minutos > 60) or (minutos < 0)


def printer_periodo(ph, pm):
    print('Período de tempo >> ', end="")
    print(ph, 'horas e', pm, 'minutos')


def calcular_duracao(inicio_h, inicio_m, final_h, final_m):

    if(entrada_nao_valida(inicio_h, inicio_m)):
        return print('Horário inicial inválido')
    if(entrada_nao_valida(final_h, final_m)):
        return print('Horário final inválido')

    minutos_inicial_total = inicio_h * 60 + inicio_m
    minutos_final_total = final_h * 60 + final_m

    if(inicio_h == final_h or inicio_h > final_h):
        print('Terminou no outro dia')

        periodo_total = ((24 * 60) - minutos_inicial_total) + \
            minutos_final_total
        periodo_h = periodo_total // 60
        periodo_m = periodo_total % 60

        printer_periodo(periodo_h, periodo_m)
    else:
        print('Terminou no mesmo dia')

        periodo_total = minutos_final_total - minutos_inicial_total
        periodo_h = periodo_total // 60
        periodo_m = periodo_total % 60

        printer_periodo(periodo_h, periodo_m)


main()
