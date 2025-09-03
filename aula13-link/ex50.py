num1 = 
for c in range(6):
    num = int(input('Digite o {}° número: '.format(c+1)))
    if num%2==0:
        num1 += num

total = sum(num1)
print('A soma dos números pares digitados é {}'.format(total))

    

