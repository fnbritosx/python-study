def ficha():
    nome = str(input('Nome do Jogador: ')).strip()
    if nome == '' or nome == '0':
        nome = '<desconhecido>'
    gols = str(input('Número de Gols: ')).strip()
    if gols == '':
        gols = 0

    print(f'O jogador {nome} fez {gols} gol(s) no campeonato!')

ficha()