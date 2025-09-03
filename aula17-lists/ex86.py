matrizona = [[], [], []]

for i in range(3):
    for j in range(3):
        valor = int(input(f'Digite um valor para [{i}, {j}]: '))
        matrizona[i].append(valor)  # adiciona na linha i já criada

# Imprime a matriz formatada
for linha in matrizona:
    for valor in linha:
        print(f'{valor:^5}', end='')
    print()
