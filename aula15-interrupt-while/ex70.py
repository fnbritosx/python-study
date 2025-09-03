print('-'*40)
print('LOJA DO SUPER BARATÃO'.center(40))
print('-'*40)

soma_total = 0
preco_maior = 0
menor_preco = 0
contador = 0

nome_menor_prod = ''

while True:
    contador += 1
    nome_prod = str(input('Nome do Produto: '))

    preco_prod = float(input('Preço: ')) 
    soma_total += preco_prod
    

    if preco_prod > 1000:
        preco_maior += 1
    if contador == 1:
        menor_preco = preco_prod
        nome_menor_prod = nome_prod
    else:
        if preco_prod < menor_preco:
            menor_preco = preco_prod
            nome_menor_prod = nome_prod

    question = input('Quer continuar? [S/N] ').strip().lower()
    while question not in ('s', 'n'):
        question = input('Quer continuar? [S/N] ').strip().lower()

    if question == 'n': 
        print('FIM DO PROGRAMA'.center(40, '-'))
        print(f'O total da compra foi R${soma_total:.2f}')
        print(f'Temos {preco_maior} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi R${menor_preco} que custa {nome_menor_prod}')
        break


