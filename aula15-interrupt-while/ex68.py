import random

user = 0
choice = ''
count = 0

while True:
    pc = random.randint(1, 10)
    user = int(input('Digite um valor: '))
    sum = pc + user
    choice = str(input('Par ou Ímpar? [P/I] ')).lower().strip()
    if sum%2 == 0 and  choice == 'p':
        count += 1
        print('-'*20)
        print(f'You played {user} and the PC {pc}. Total of {sum} DEU PAR')
        print('-'*20)
        print('You WIN!')
        print('Let\'s play again...')
        print('-='*20)
    elif sum%2 == 1 and choice == 'i':
        count += 1
        print('-'*20)
        print(f'You played {user} and the PC {pc}. Total of {sum} DEU ÍMPAR')
        print('-'*20)
        print('You WIN!')
        print('Let\'s play again...')
        print('-='*20)
    elif sum%2 == 0 and  choice == 'i':
        print('-'*20)
        print(f'You played {user} and the PC {pc}. Total of {sum} DEU PAR')
        print('-'*20)
        print(f'You LOST! You won {count} times')
        print('-='*20)
        break
    elif sum%2 == 1 and  choice == 'p':
        print('-'*20)
        print(f'You played {user} and the PC {pc}. Total of {sum} DEU ÍMPAR')
        print('-'*20)
        print(f'You LOST! You won {count} times')
        print('-='*20)
        break




