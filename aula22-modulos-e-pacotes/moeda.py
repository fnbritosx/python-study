def resumo(a, b, c):
    print('-'*40)
    print('RESUMO DO VALOR'.center(30))
    print('-'*40)

    print(f'{"Preço a ser analisado:".ljust(30)} R${a:.2f}' )

    dobro = a * 2
    print(f'{"Dobro do preco".ljust(30)} R${dobro:.2f}' )

    metade = a / 2
    print(f'{"Metade do preco".ljust(30)} R${metade:.2f}' )

    aumento = a * 1.8
    print(f'{str(b)}% de aumento:'.ljust(30), f'R${aumento:.2f}' )

    reducao = a * 0.35
    print(f'{str(c)}% de redução:'.ljust(30), f'R${reducao:.2f}' )

    print('-'*40)

