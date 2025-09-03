time = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Bahia', 'Fluminense',  
    'Atlético-MG', 'Botafogo', 'Mirassol', 'Corinthians', 'Grêmio', 'Ceará','Vasco',
    'São Paulo', 'Santos', 'Vitória', 'Internacional', 'Fortaleza', 'Juventude', 'Sport')

for c in range(0, 5):
    print(time[c], end=' ')

print('\n' +'='*40)

for c in range(1, 5):
    print(time[-c], end=' ')

print('\n' + '='*40)

print(sorted(time))

print('\n' + '='*40)

pos = time.index('Corinthians') + 1

print(f'O time Corinthians está no {pos}º lugar.')
