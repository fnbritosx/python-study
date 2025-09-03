def voto():
    from datetime import date
    ano_nasc = int(input('Ano de nascimento: '))

    idade = date.today().year - ano_nasc

    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA.')
    elif 16 <= idade < 18 or idade >= 65:
        print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        print(f'Com {idade} anos: VOTO OBRIGATÓRIO.') 
 
voto()