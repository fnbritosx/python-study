import math
n1 = float(input('Digite o valor de um ângulo: '))

csen = math.radians(n1)
ccos = math.radians(n1)
ctg = math.radians(n1)

seno = math.sin(csen)
cos = math.cos(ccos)
tg = math.tan(ctg)

print('O angulo é {}°, o valor do seno = {:.2f}, cosseno = {:.2f}, tangente {:.2f}'.format(n1, seno, cos, tg))
