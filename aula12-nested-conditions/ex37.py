num = int(input('Digite um número: '))

print('Qual base deseja converter? \n 1 para binário \n 2 para octal \n 3 para hexadecimal \n')
conversao = int(input('Sua opção: '))

if conversao == 1:
    print('O número binário de {} é {}'.format(num, bin(num)[2:]))
elif conversao == 2:
    print('O número octal de {} é {}'.format(num, oct(num)[2:]))
else:
    print('O número hexadecimal de {} é {}'.format(num, hex(num)[2:]))