import sympy

num = int(input('Digite um número: '))

if sympy.isprime(num):
    print('{} é primo!'.format(num))
else:
    print('{} não é primo.'.format(num))
