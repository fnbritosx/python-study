numeros = [[], []]

for c in range(7):
    n = int(input(f'Digite o {c+1}° valor: '))
    if n%2==0:
        numeros[0].append(n)
    else: 
        numeros[1].append(n)
        

numeros[0].sort()
numeros[1].sort()


print(f'Os valores pares digitados foram {numeros[0]}')

print(f'Os valores ímpares digitados foram {numeros[1]}')



 
