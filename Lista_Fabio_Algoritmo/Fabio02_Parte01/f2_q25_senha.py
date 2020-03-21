#Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. O algoritmo deve escrever uma mensagem de permissão de acesso ou não.

def main():
    senha = int(input('Digite sua senha >> '))

    if( senha != 1234 ):
        print('Senha Inválida')
    else:
        print('Acesso concedido. Bem vindo')



main()