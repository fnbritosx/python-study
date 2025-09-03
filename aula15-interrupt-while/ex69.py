print('-'*40)
print('CADASTRE UMA PESSOA'.center(40))
print('-'*40)

response = 's'
count_age = 0
count_f = 0
count_m = 0

while True:
    age = 0
    gender = ''
    if response == 's':
        age = (int(input('Idade: ')))
        if age > 18:
            count_age += 1

        gender = str(input('Sexo: [M/F] ')).strip().lower()

        while gender not in ('m', 'f'):
            gender = str(input('Sexo: [M/F] ')).strip().lower()

        if gender == 'm':
            count_m += 1
        if age < 21 and gender == 'f':
            count_f += 1

        response = str(input('Quer continuar? [S/N] '))

        while response not in ('s') and not response == 'n':
            response = str(input('Quer continuar? [S/N] ')).strip().lower()

        print('-'*40)
        print('CADASTRE UMA PESSOA'.center(40))
        print('-'*40)
        
    elif response == 'n':
        print('FIM DO PROGRAMA'.center(40, '='))
        print(f'Total de pessoas com mais de 18 anos: {count_age}')
        print(f'Ao todo temos {count_m} homens cadastrados')
        print(f'E temos {count_f} mulheres com menos de 20 anos')
        break
