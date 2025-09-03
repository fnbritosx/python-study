def notas(* notas, sit=False):
    fifa = {}

    fifa['total'] = len(notas)
    fifa['maior'] = max(notas)
    fifa['menor'] = min(notas)
    fifa['media'] = sum(notas) / len(notas)

    if sit == True:
        if fifa['media'] > 7:
            fifa['situação'] = 'BOA'
        elif fifa['media'] < 7 and fifa['media'] > 5:
            fifa['situação'] = 'RAOAVEL'
        else:
            fifa['situação'] = 'RUIM'
            
    return print(fifa)

resp = notas(3.5, 2, 6.5, sit=False)


    
