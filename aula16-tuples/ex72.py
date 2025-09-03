from num2words import num2words
num = tuple(range(0,21))

user = int(input('Digite um número entre 0 e 20: '))
while user > 20 or user < 0:
    user = int(input('Tente novamente. Digite um número entre 0 e 20: '))

for c in num:
    extenso = num2words(c, lang='pt_BR')
    if user == c:
        print(f'Você digitou o número {extenso}')