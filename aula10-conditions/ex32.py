import datetime
ano = int(input('Digite um ano ou coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year

if ano % 400 == 0:
    print('O ano {} é Bissexto!'.format(ano))
elif ano % 100 == 0:
    print('O ano {} NÃO é Bissexto!'.format(ano))
elif ano % 4 == 0:
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} NÃO é Bissexto!'.format(ano))

#OUTRA FORMA DE CALCULAR SE O ANO É BISSEXTO

ano = int(input('Digite um ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é Bissexto!'.format(ano))  
else:
    print('O ano {} NÃO é Bissexto!'.format(ano))

