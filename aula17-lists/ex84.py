pessoas = []
nome_pesado = []
nome_leve = []

while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))
    pessoas.append([nome, peso])  # Armazena como sublista: [nome, peso]

    resposta = input('Deseja continuar? [S/N] ').strip().lower()
    if resposta == 'n':
        break

# Inicializa com o primeiro peso cadastrado
maior = pessoas[0][1]
menor = pessoas[0][1]

for p in pessoas:
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
        menor = p[1]

# Coleta quem são os mais pesados e mais leves
for p in pessoas:
    if p[1] == maior:
        nome_pesado.append(p[0])
    if p[1] == menor:
        nome_leve.append(p[0])

print(f'\n{len(pessoas)} pessoas foram cadastradas.')
print(f'O maior peso foi {maior}kg. Peso de: {", ".join(nome_pesado)}')
print(f'O menor peso foi {menor}kg. Peso de: {", ".join(nome_leve)}')
