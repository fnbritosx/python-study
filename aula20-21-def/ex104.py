def leiaInt(a):
    n = str(input('Digite um número: '))
    while not n.isnumeric():
        print('ERRO! Digite um número inteiro.')
        n = input('Digite um número: ')
    return n
            
       

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')