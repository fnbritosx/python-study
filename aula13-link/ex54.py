import datetime

maior_idade = 0
menor_idade = 0
ano_atual = datetime.datetime.now().year

for c in range(7):
    ano_nasc = int(input('Digite o ano de nascimento da {}° pessoa: ').format(c+1))
    idade = ano_atual - ano_nasc
    
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1

print(f'{maior_idade} são maiores de idade')
print(f'{menor_idade} são menores de idade')
