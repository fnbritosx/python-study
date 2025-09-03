sexo = str(input('Digite seu sexo: [M/F] ')).lower().strip()[0]

while sexo not in ['m', 'f']:
    sexo = input('Dados Inválidos. Por favor, informe seu sexo: ')  

print(f'Sexo {sexo.upper()} registrado com sucesso!')


