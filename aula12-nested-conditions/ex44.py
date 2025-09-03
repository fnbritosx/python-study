preco_prod = float(input('Digite o valor do produto: '))
pagamento = int(input('FORMAS DE PAGAMENTO \n [ 1 ] à vista dinheiro/cheque \n [ 2 ] à vista cartão \n [ 3 ] 2x no cartão \n [ 4 ] 3x ou mais no cartão \n Qual é a opção? '))


if pagamento == 1: 
    dinheiro_cheque = preco_prod  * 0.9
    print('Sua compra de {} vai custar {} no final.'.format(preco_prod, dinheiro_cheque))
elif pagamento == 2:
    cartao_vista = preco_prod * 0.95
    print('Sua compra de {} vai custar {} no final.'.format(preco_prod, cartao_vista))
elif pagamento == 3:
    cartao_parcela = preco_prod / 2
    print('Sua compra de {} vai custar {} no final.'.format(preco_prod, cartao_parcela))
elif pagamento == 4:
    parcela = int(input('Quantas parcelas? '))
    cartao_parcela = preco_prod * 1.20
    pg_mes = cartao_parcela / parcela
    print('Sua compra será parcelada em {}x de {} COM JUROS \n Sua compra de R${} vai custar R${} no final'.format(parcela, pg_mes, preco_prod, cartao_parcela))
