import random

print('-'*40)
print('JOGA NA MEGA SENA'.center(40))
print('-'*40)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))

count = 0

while count < jogos:
    pc = random.sample(range(1, 61), 6)
    print(f'Jogo {count + 1}: {pc}')
    count += 1

print(' < BOA SORTE > '.center(40, '='))

    
    


        


