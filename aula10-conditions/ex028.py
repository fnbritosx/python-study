import random
aletatorio = random.randint(0,5)

user = int(input('Em que número pensei? '))

if user == aletatorio:
    print('PROCESSANDO... \n O computador escolheu o valor {} e você escolheu {}. Você venceu!'.format(aletatorio, user))
else:
     print('PROCESSANDO... \n O computador escolheu o valor {} e você escolheu {}. Você perdeu!'.format(aletatorio, user))
