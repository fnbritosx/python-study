alunos = []

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) /2

    alunos.append([nome, [n1, n2], media])

    resp = str(input('Quer continuar? [S/N] ')).lower().strip()

    if resp == 'n':
        print ('-='*40)
        print('No. NOME     MÉDIA')
        print('-'*20)
        for pos, valor in enumerate(alunos, 0):
            print(f'{pos} {valor[0]} {valor[2]}')    
        resp2 = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        while resp2 != 999:
            for idx, nota in enumerate(alunos, 0):
                
                print(f'Notas de {nota[0]} são {nota[1]}')
            resp2 = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        else:
            print('FINALIZANDO...')
            break