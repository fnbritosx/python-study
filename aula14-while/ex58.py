import random

pc = random.randint(0, 10)
user = int(input('Digite o número que eu pensei: '))
counter = 1

while user != pc:
    counter += 1
    if user > pc:
        user = int(input('Menos.. eu pensei em um número um pouco menor. \nDigite o número que eu pensei:'))
    else: 
        user= int(input('Mais.. eu pensei em um número um pouco maior. \nDigite o número que eu pensei: '))
print('Eu pensei no número {}, você acertou com {} tentativas.'.format(pc, counter))
    