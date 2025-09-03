jogador = {}

jogador['nome'] = str(input('Nome do jogador: '))

partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

lista_gols = []
jogador['gols'] = lista_gols

count = 0
total_gols = 0
while count < partidas:
    gols = int(input(f'Quantos gols na partida {count + 1}? '))
    lista_gols.append(gols)
    total_gols += gols
    count += 1

jogador['total'] = total_gols

print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('-='*30)

print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')

for idx, valor in enumerate(lista_gols,1):
    print(f'Na partida {idx}, fez {valor} gols.')
    
print(f'Foi um total de {total_gols} gols.')