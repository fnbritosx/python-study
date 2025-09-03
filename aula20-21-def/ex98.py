def crescente():
    print('Contagem de 1 até 10 de 1 em 1')

    for cont in range(1, 11):
        print(cont, end=' ')

    print()


def decrescente():
    print('Contagem de 10 até 1 de 1 em 1')

    for cont in range(10, 0, -1):
        print(cont, end = ' ')

    print()

def personalizado():
    print('Agora é sua vez de personalizar a contagem!')

    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    fim += 1

    if passo == 0:
        passo = 1
    
    if inicio > fim:
        passo = -abs(passo)
        fim -= 2

    for cont in range(inicio, fim, passo):
        print(cont, end=' ')

    print()

crescente()
decrescente()
personalizado()
        