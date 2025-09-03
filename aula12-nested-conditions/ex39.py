import datetime

ano = int(input('Digite o ano que você nasceu: '))
ano_atual = datetime.datetime.now().year
idade = ano_atual - ano
alistamento = 18 - idade

if ano >= 2008:
    print('Quem nasceu em {} tem {} anos em {} \n Ainda faltam {} anos para o alistamento \n Seu alistamento será em '.format(ano, idade, ano_atual, abs(alistamento)))
elif ano == 2007:
    print('Quem nasceu em {} tem {} anos em {} \n Ainda faltam {} anos para o alistamento '.format(ano, idade, ano_atual, abs(alistamento)))
else: 
    print('Já passou do tempo do alistamento.')
 


