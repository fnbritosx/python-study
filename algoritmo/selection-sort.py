def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range (1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    print(menor)
    print(menor_indice)

lista = [5, 7, 3, 0, 6]   
buscaMenor(lista)