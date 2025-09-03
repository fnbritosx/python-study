a = float(input(('Digite o valor do primeiro segmento de reta: ')))
b = float(input(('Digite o valor do segundo segmento de reta: ')))
c = float(input(('Digite o valor do terceiro segmento de reta: ')))

if a + b > c and a + c > b and  b + c > a:
    print('É possivel formar um triângulo com os valores {}, {}, {}'.format(a, b, c))
else:
    print('Não é possível formar triangulo com os valores {}, {}, {}'.format(a, b, c))