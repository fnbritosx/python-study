teste = []

teste.append('Fernando')
teste.append(19)


teste2 = []

teste2.append(teste[:])

teste[0] = 'Joao'
teste[1] = 10

teste2.append(teste)

print(teste2)
