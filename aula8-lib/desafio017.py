import math
n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjacente: '))

hip = math.sqrt(n1 ** 2 + n2 ** 2)

print('Um cateto é {}, o outro é {} logo a hipotenusa é {:.2f}'.format(n1, n2, hip))