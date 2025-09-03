from time import sleep

num1 = int(input('Digite o 1° valor: '))
num2 = int(input('Digite o 2° valor: '))
menu = 0

while menu != 5:
    print('\n[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')

    menu = int(input('O que deseja? '))

    if menu == 1:
        print(f'A soma de {num1} + {num2} = {num1 + num2}')
        sleep(1)

    elif menu == 2:
        print(f'A multiplicação de {num1} x {num2} = {num1 * num2}')
        sleep(1)

    elif menu == 3:
        maior = max(num1, num2)
        print(f'O maior entre {num1} e {num2} é {maior}')
        sleep(1)

    elif menu == 4:
        num1 = int(input('Digite o novo 1° valor: '))
        num2 = int(input('Digite o novo 2° valor: '))
        sleep(1)

    elif menu == 5:
        print('Finalizando...')
        sleep(1)  

    else:
        print('Opção inválida! Tente novamente.')
        sleep(1)

print('Programa encerrado.') 

    

        
    