
from time import sleep

def ajuda():

    while True:

        a = 'SISTEMA DE AJUDA PYHELP'

        print('~'* (len(a) + 10))
        print(a.center(len(a) + 10))
        print('~'* (len(a) + 10))

        lib = str(input('Função ou Biblioteca > ')).lower().strip()
        sleep(0.5)
        

        if lib != 'fim':
            b = f'Acessando o manual do comando {lib}'

            print('~'* (len(a) + 10))
            print(b.center(len(a) + 10))
            print('~'* (len(a) + 10))

            sleep(0.5)

            help(lib)

        else:
            c = 'ATÉ LOGO!'

            print('~'* (len(c) + 10))
            print(c.center(len(c) + 10))
            print('~'* (len(c) + 10))

            sleep(0.5)

            break
    
ajuda()