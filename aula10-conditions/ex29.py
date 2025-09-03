v = int(input('Qual velocidade você atingiu? '))


if v > 80:
    multa = 7 * (v - 80)
    print('Você foi multado! Deverá pagar {} reais.'.format(multa))
else:
    print('Você digiriu com responsabilidade. Parabens!')