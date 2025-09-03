a = input('Digite algo: ')

print('O tipo primitivo desse \'algo\' é {}'.format(type(a))) #Tipo da str digitada.
print('Só tem espaços? {}'.format(a.isspace())) #Se só tem espaços
print('É um número? {}' .format(a.isnumeric())) #Se só tem números.
print('É alfabético? {}'.format(a.isalpha())) #Se tem letras.
print('É alfanumérico? {}'.format(a.isalnum())) #Se é alfanumérico (Contém letras ou números ou ambos).
print('Está em maiúsculas? {}'.format(a.isupper())) #Se é tudo maiúsculo.
print('Está em minúsculas? {}'.format(a.islower())) #Se é tudo minúsculo.
print('Está capitalizada? {}'.format(a.istitle())) #Se está capitalziada como título. A primeira letra tem que ser maiúscula e o resto tem que ser minúsculo.