_num = 0
soma = 0

while True:
    _num = int(input('Digite um número: '))
    if _num == 999:
        break
    soma += _num
print(f'A soma dos números foi de {soma}')
