l = float(input('Digite a largura: '))
h = float(input('Digite a altura: '))

area = l * h
tinta = area * 0.5

print('A largura é {0}, a altura é {1}, a área é {2}, você precisará de {3}L de tinta para pintar a área.'.format(l, h, area, tinta))