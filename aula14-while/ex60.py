num1 = int(input('Digite um número: '))
c = num1
fatorial = 1
while c > 0:
    
    print('{}'.format(c), end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='') 
    fatorial *= c
    c -= 1
    
print(fatorial)
    
   

    
