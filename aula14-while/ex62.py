print('10 TERMOS DE UMA PA')
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 0
while c < 10:
    c += 1
    print(termo, end=' -> ')
    termo += razao
print('PAUSA', end='')

num = 1

while num > 0:
    num = int(input('\nQuantos termos você quer mostrar a mais? '))
    
    for c in range(num):
        print(termo, end=' -> ')
        termo += razao
    print('PAUSA2', end='')

else:
    print('\nO programa será finalizado...')
    print('Obrigado!')


