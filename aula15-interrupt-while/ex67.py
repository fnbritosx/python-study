_num = 0
tabuada = 1
count = 1

while True:
    _num = int(input('Digite um número: '))
    if _num > 0:
        while count < 11:
            resultado = _num * count
            print (f'{_num} x {count} = {resultado}')
            count += 1
    else:
        break
print('O programa será finalizado.')







