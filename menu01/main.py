from time import sleep
print('Digite dois valores inteiros')
n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
resp = 0
while resp != 5:
    print('Agora escolha uma das opções')
    print('[ 1 ] - Somar')
    print('[ 2 ] - Multiplicar')
    print('[ 3 ] - Maior Número')
    print('[ 4 ] - Novos Números')
    print('[ 5 ] - Sair do Programa')
    resp = int(input('Opção: '))

    if resp == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
        sleep(3)
    elif resp == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
        sleep(3)
    elif resp == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        print('Entre {} e {} o maior número é: {}'.format(n1, n2, maior))
        sleep(3)
    elif resp == 4:
        print('Digite dois valores inteiros')
        n1 = int(input('Valor 1: '))
        n2 = int(input('Valor 2: '))
        sleep(1)
    elif resp == 5:
        print('Programa encerrando...')
        sleep(3)
    else:
        print('\033[31mValor Inválido! Tente Novamente!\033[m')

    print('=-=' * 10)
print('Fim do Programa.')
