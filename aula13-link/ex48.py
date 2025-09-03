n = 0
n1 = 0
for c in range (1, 501):
    if c%2 == 1 and c%3 == 0:
        n += c
        n1 += 1
print(n1, n)
print('FIM')
