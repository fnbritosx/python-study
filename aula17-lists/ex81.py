resposta = 's'
lista = []

while resposta == 's':
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    resposta = str(input('Deseja continuar? [S/N] ')).lower().strip()

lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos')             # lista.sort() ordena a lista original, mas NÃO retorna nada.
print(f'Os valores em ordem decrescente são {lista}')   # sorted(lista) retorna uma nova lista ordenada, sem mudar a original.

if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 NÂO faz parte da lista!')

