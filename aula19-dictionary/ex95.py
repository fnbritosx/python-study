jogadores = []

while True:
    jogador = {}
    gols = []

    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador['nome']} jogou? '))

    for c in range(1, partidas + 1):
        gol = int(input(f'Quantos gols na partida {c}? '))
        gols.append(gol)
        
        jogador['gols'] = gols
        jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())

    resposta = str(input('Quer continuar? [S/N] ')).strip().lower()
    if resposta == 'n':
        break

print(f"{'cod':<5} {'nome':<15} {'gols':<20} {'total':>5}")
print('-'*50)

for idx, jogador in enumerate(jogadores):
    print(f"{idx:<5} {jogador['nome']:<15} {str(jogador['gols']):<20} {jogador['total']:>5}")


