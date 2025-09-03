valor_casa = float(input('Digite o valor da casa: '))
salario = float(input('Quanto recebe? R$ '))
quitar_ano = int(input('Em quantos anos pretente quitar a casa? '))

quitar_mes = quitar_ano * 12

prestacao = valor_casa / quitar_mes

excedente = salario * 0.3


print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.3f}'.format(valor_casa, quitar_ano, prestacao))


if prestacao > excedente:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo APROVADO!')

