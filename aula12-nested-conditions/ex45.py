import random
import time
pc = random.randint(0,2)
if pc == 0:
    pc = 'Pedra'
if pc == 1:
    pc = 'Papel'
if pc == 2:
    pc = 'Tesoura'
user = int(input('Suas Opções: \n [ 0 ] PEDDRA \n [ 1 ] PAPEL \n [ 2 ] TESOURA \n Qual é a sua jogada? '))
if user == 0:
    user = 'Pedra'
if user == 1:
    user = 'Papel'
if user == 2:
    user = 'Tesoura'
print(pc, user)
print(' JO ') 
time.sleep(1) 
print('KEN')  
time.sleep(1)
print('PO!!!') 
time.sleep(1) 
print('-=' * 11)

if pc == user:
    print('Computador jogou {} \nJogador jogou {}'.format(pc, user))
    print('-=' * 11)
    print('EMPATOU!')
elif pc == 'Pedra' and user == 'Papel':
    print('Computador jogou {} \nJogador jogou {}'.format(pc, user))
    print('-=' * 11)
    print('JOGADOR VENCE!')
elif pc == 'Pedra' and user == 'Tesoura':
    print('Computador jogou {} \nJogador jogou {}'.format(pc, user))
    print('-=' * 11)
    print('COMPUTADOR VENCE!')
elif pc == 'Papel' and user == 'Pedra':
    print('Computador jogou {} \nJogador jogou {}'.format(pc, user))
    print('-=' * 11) 
    print('COMPUTADOR VENCE!')
elif pc == 'Papel' and user == 'Tesoura':
    print('Computador jogou {} \nJogador jogou {}'.format(pc, user))
    print('-=' * 11)
    print('JOGADOR VENCE!')
elif pc == 'Tesoura' and user == 'Pedra':
    print('Computador jogou {} \nJogador jogou {}'.format(pc, user))
    print('-=' * 11)
    print('JOGADOR VENCE!')
elif pc == 'Tesoura' and user == 'Papel':
    print('Computador jogou {} \nJogador jogou {}'.format(pc, user))
    print('-=' * 11)
    print('COMPUTADOR VENCE!')
