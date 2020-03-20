# Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maiorou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a médiafinal. Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deveescreva “Reprovado”.


def main():
    nota1 = int(input('nota >> '))
    nota2 = int(input('nota >> '))

    media_notas = media_nt(nota1, nota2)

    if passou_na_prova( media_notas ):
        print('Aprovado, Parabéns !!!')
    else:
        nota_exame = int(input('Nota no exame >> '))
        if passou_no_exame( nota_exame, media_notas):
            print('Aprovado !, mas estude mais da próxima :)')
        else:
            print('Reprovado :(')


def media_nt(nota1, nota2):
    return (nota1 + nota2)/2


def passou_na_prova(media):
    if(media >= 7):
        return True
    else:
        return False


def passou_no_exame(nt_exame, media_notas):
    media_final = media_nt( nt_exame, media_notas )
    if media_final >= 5:
        return True
    else:
        return False


main()