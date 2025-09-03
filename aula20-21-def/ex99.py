from time import sleep

def maior(* numeros):
    print('Analisando os valores passados...')
    sleep(1)
    print(*numeros, f'Foram informados {len(numeros)} ao todo.')
    sleep(1)
    print(f'O maior valor informado foi {max(numeros)}.')
    sleep(1)
    print('-='* 30)

print('-='*30)
maior(2, 3, 4, 5, 10, 15)
maior(4, 7, 0)
maior(6)
maior( -5, -2, -1)