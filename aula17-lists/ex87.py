matrizona = [[], [], []]
sum_par = 0
sum_coluna = 0
maior_num = 0

for i in range(3):
    for j in range(3):
        valor = int(input(f'Digite um valor para [{i}, {j}]: '))
        if valor % 2 ==0:
            sum_par += valor
        matrizona[i].append(valor)  
        
for linha in matrizona:
    if valor -1:
            sum_coluna += valor
    for valor in linha:
        print(f'{valor:^5}', end='')
    print()

for num in matrizona[1]:
     if num > maior_num:
          maior_num = num

print(f'A soma dos valores pares é {sum_par}')
print(f'A soma dos valores da terceira coluna é {sum_coluna}')
print(f'O maior valor da segunda linha é {maior_num}')