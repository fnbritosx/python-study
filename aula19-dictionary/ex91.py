import random

jogadas = {}

participantes = int(input('Quantos jogadores irão participar? '))

print('Valores sorteados: ')

for i in range(1, participantes + 1):
    dado = random.randint(1, 6)
    jogadas[f'Jogador {i}'] = dado

for j, d in jogadas.items():
    print(f'O {j} tirou {d}')


print('Ranking dos jogadores: ')



