tupla = ()
tupla2 = ()
count1 = 0
count2 = 0


for c in range (1, 6):
    num = int(input(f'Digite o {c}° valor: '))
    tupla += (num,)
    if num%2==0:
        tupla2 += (num,)

if 9 in tupla:
    count1 += 1

print(f'Você digitou os valores {tupla}')
print(f'O número 9 apareceu {count1} vezes')

if 3 in tupla:
    pos = tupla.index(3) + 1  # +1 se quiser posição "humana" (começando de 1)
    print(f"O número 3 está na posição {pos}")
else:
    print("O número 3 não está na tupla.")

print(f'Os valores pares digitados foram {tupla2}')

    


