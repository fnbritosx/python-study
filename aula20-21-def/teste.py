def dobra(lst):
    pos = 0 
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

lista = [2, 3, 4, 5]
original = lista.copy()

dobra(lista)
print(lista)

print(original)

