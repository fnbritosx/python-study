pessoal = []
pessoas = {}
mulheres = []

qt_pessoas = 0
total_idade = 0

while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: '))
    pessoas['idade'] = int(input('Idade: '))
    pessoal.append(pessoas.copy())


    if pessoas['sexo'] == 'f':
        mulheres.append(pessoas['nome'])

    qt_pessoas += 1
    total_idade += pessoas['idade']

    resposta = str(input('Quer continuar? [S/N] ')).strip().lower()

    if resposta == 'n':
        break

media_idade = total_idade / qt_pessoas

print(f'O grupo tem {qt_pessoas} pessoas.')
print(f'A média de idade é de {media_idade:.2f}')
print(f'As mulheres cadastradas foram: {', '.join(mulheres)}')

for valor in pessoal:
    if valor['idade'] > media_idade:
        print(f"Nome = {valor['nome']}; Sexo = {valor['sexo']}; Idade = {valor['idade']};")



