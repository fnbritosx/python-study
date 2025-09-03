print('10 TERMOS DE UMA PA')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 0
while c < 10:
    c += 1
    print(termo, end=' -> ')
    termo += razao
print('FIM', end='')