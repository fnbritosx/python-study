viagem = float(input('Qual é a distancia da viagem em KM? '))

preco1 = viagem * 0.50
preco2 = viagem * 0.45

if viagem <= 200:
    print('O preço para {} KM percorrido será de R${:.2f}'.format(viagem, preco1))
else:
    print('O preco para {} KM percorrido será de R${:.2f}'.format(viagem, preco2))