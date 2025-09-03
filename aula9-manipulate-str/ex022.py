nome = str(input('Digite o seu nome completo: ')).strip() #strip vai tirar os espaços no começo e no final

#Pega o nome digitado e coloca todas as letras em maiúsculas 
print('O seu nome com todas as letras maiúsculas é: {} '.format(nome.upper()))

#Pega o nome digitado e coloca todas as letras em minúsculas
print('o seu nome com letras minúsculas é: {}'.format(nome.lower()))

#Conta quantas letras tem excluindo espaços
print('O seu nome tem {} letras ao todo'.format(len(nome) - nome.count(' '))) #Os espaços no começo e final foram retirados, porém sobrou os espaços do meio. o nome.count(' ') foi inserido para retirar os espaços entre as palavras.

# 1° forma de calcular o número de letras do primeiro nome.
#Conta ate o primeiro espaço, o index do espaço é o mesmo número de letras do seu primeiro nome. (index começa no 0)
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

# 2° forma de calcular o número de letras do primeiro nome.
#Separa em listas (INDEX NO PYTHON SEMPRE COMEÇA NO 0)
sep = nome.split()

#Após separar o que foi digitado em listas, conta quantas letras tem na primeira palavra digitada (para isso o '[0]' foi colcoado ao final para selecionar a primeira palavra escolhida)
print('O primeiro nome é {} e tem {} letras'.format(sep[0], len(sep[0])))