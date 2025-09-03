salario = float(input('Digite o seu salário: '))

if salario > 1250:
    ajuste = salario * 0.1
    novo = salario + ajuste
    print('O seu novo salario é de R${}'.format(novo))
else:
    ajuste1 = salario * 0.15
    novo1 = salario + ajuste1 
    print('O seu novo salario é de R${}'.format(novo1))
