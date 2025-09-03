from random import sample

lista = list()

def sorteia():
    aleatorio = sample(range(1, 10), 5)
    print('Sorteando 5 valores da lista:', * aleatorio,  'PRONTO!')
    #1 método (o append aceita apenas 1 argumento por vez, no aleatorio há 5. 
    # logo, será necessario fzr um looping).
    #for c in aleatorio:
        #lista.append(c)
    #2 metodo
    #extend passa os argumentos 1 por vez, bem mais simples.
    lista.extend(aleatorio)

def somaPar():
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista}, temos {soma}')

sorteia()
somaPar()
