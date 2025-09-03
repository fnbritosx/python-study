lista = []
lista_par = []
lista_impar = []

while True:
    valor = int(input('Digite o valor: '))
    lista.append(valor)
    if valor%2==0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
    resposta = input('Dseja continuar? [S/N] ').strip().lower()
    if resposta =='n':
        break

print(f'Os valores da lista são {lista}')
print(f'Os valores pares são {lista_par}')
print(f'Os valores pares são {lista_impar}')
    