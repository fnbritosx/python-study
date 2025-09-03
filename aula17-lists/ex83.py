lista = []
cont1 = 0
cont2 = 0
pos = 0

expressao = input('Digite a sua expressão: ')
lista.append(expressao)

# Corrigido: percorrer os caracteres da string dentro da lista
while pos < len(lista[0]):
    if lista[0][pos] == '(':
        cont1 += 1
    elif lista[0][pos] == ')':
        cont2 += 1
    pos += 1

if cont1 == cont2:
    print('A sua expressão é válida!')
else:
    print('A sua expressão é inválida!')
