pessoas = []

while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    pessoas.append([nome, peso])

    resposta = str(input('Deseja continuar [S/N] ')).strip().lower()

    if resposta == 'n':
        break

maior_valor = pessoas[0][1]
nome_maior = []

for p in pessoas:
    if p[1] > maior_valor:
        nome_maior = []
        maior_valor = p[1]
        nome_maior.append(p[0])
    elif p[1] == maior_valor:
        nome_maior.append(p[0])
        

menor_valor = pessoas[0][1]
nome_menor = []

for p in pessoas:
    if p[1] < menor_valor:
        nome_menor = []
        menor_valor = p[1]
        nome_menor.append(p[0])
    elif p[1] == menor_valor:
        nome_menor.append(p[0])
        

print(f'Ao todo você cadastrou {len(pessoas)}.')
print(f'O maior peso foi de KG {maior_valor}. Pesos de {nome_maior}')
print(f'O menor peso foi de KG {menor_valor}. Pesos de {nome_menor}')

