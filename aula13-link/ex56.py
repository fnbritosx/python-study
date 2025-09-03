nome = []
idade = []
sexo = []

nome_velho = ''
idade_velho = 0
abaixo = 0

for c in range(4):
    n = str(input('Digite o nome do {}° usuário: '.format(c+1))).strip().lower()
    nome.append(n)
    id = int(input('Digite a idade do {}° usuário: '.format(c+1)))
    idade.append(id)
    sx = str(input('Digite o sexo do {}° usuário: '.format(c+1))).strip().lower()
    sexo.append(sx)

    if sx == 'm' and id > idade_velho:
            idade_velho = id
            nome_velho = n
    if sx == 'f' and id < 20:
        abaixo += 1


media = sum(idade) / len(idade)

print(media)  
print(nome_velho)
print(abaixo)



