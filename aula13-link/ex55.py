pesos = []

for c in range(5):
    p = float(input('Quanto pesa a {}° pessoa? KG'.format(c+1)))
    pesos.append(p)

maior_peso = max(pesos)
menor_peso = min(pesos)

print(maior_peso)
print(menor_peso)
