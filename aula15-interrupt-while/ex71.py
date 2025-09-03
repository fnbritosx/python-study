print('='*40)
print('BANCO DO BENÉ'.center(40))
print('='*40)

sacar = int(input('Qual valor você quer sacar? R$'))

if sacar%50 == 0:
    print (f'Total de {sacar//50} cédulas de R$50')
    print('='*40)
    print('Volte sempre ao BANCO DO BENÉ! Tenha um bom dia!')
else:
    if sacar//50 > 0:
        print (f'Total de {sacar//50} cédulas de R$50')
    resto_50 = sacar - 50 * (sacar//50)
    if resto_50%20 == 0:
       print (f'Total de {resto_50//20} cédulas de R$20') 
       print('='*40)
       print('Volte sempre ao BANCO DO BENÉ! Tenha um bom dia!')
    else:
        if resto_50//20 > 0:
            print (f'Total de {resto_50//20} cédulas de R$20')  
        resto_20 = resto_50 - 20 * (resto_50//20)
        if resto_20%10 == 0:
            print (f'Total de {resto_20//10} cédulas de R$10') 
            print('='*40)
            print('Volte sempre ao BANCO DO BENÉ! Tenha um bom dia!')
        else:  
            if resto_20//10 > 0:
                print (f'Total de {resto_20//10} cédulas de R$10') 
            resto_10 = resto_20 - 10 * (resto_20//10)
            print (f'Total de {resto_10//1} cédulas de R$1')
            print('='*40)
            print('Volte sempre ao BANCO DO BENÉ! Tenha um bom dia!')
    
            

            