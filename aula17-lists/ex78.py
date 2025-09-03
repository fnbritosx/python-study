lista = []

for c in range(5):
    valores = int(input(f'A posição do {c}° valor: '))
    lista.append(valores)

maior_num = max(lista)
menor_num = min(lista)

pos_maior = lista.index(maior_num) 
pos_menor = lista.index(menor_num) 

print(lista)

print(f'A posição é {pos_maior} e o maior número é o {maior_num}')
print(f'A posição é {pos_menor} e o menor número é o {menor_num}')