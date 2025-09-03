palavras = (
    'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
    'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro'
)

vogais = ('a', 'e', 'i', 'o', 'u')
'''
for palavra in palavras:
    vogais_encontradas = ''
    for letra in palavra:
        if letra in vogais and letra not in vogais_encontradas:
            vogais_encontradas += letra
    print(f'Na palavra {palavra.upper()} temos as vogais: {", ".join(vogais_encontradas)}')
'''
#FORMA 2

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper():<12} temos as vogais: ', end='')
    for letra in palavra:
        if letra in 'aeiou'.lower():
            print(f'{letra}', end=' ')


