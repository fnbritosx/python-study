resposta = 's'
lista = []

while resposta == 's':
    valor = ''
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resposta = input('Deseja continuar? [S/N] ')
print(f'Você digitou os valores {sorted(lista)}')