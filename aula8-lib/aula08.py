"""
 Função              Descrição                                    Exemplo
 -------------------------------------------------------------------------------
 math.ceil(x)        Arredonda para cima                          math.ceil(4.2) → 5
 math.floor(x)       Arredonda para baixo                         math.floor(4.8) → 4
 math.trunc(x)       Trunca (remove a parte decimal)              math.trunc(4.9) → 4
 math.fabs(x)        Valor absoluto (sempre positivo)             math.fabs(-10) → 10.0
 math.factorial(x)   Fatorial de um número inteiro positivo       math.factorial(5) → 120
 math.sqrt(x)        Raiz quadrada                                math.sqrt(9) → 3.0
 math.pow(x, y)      Potência (x elevado a y)                     math.pow(2, 3) → 8.0
 math.log(x, base)   Logaritmo (base padrão é o número de Euler)  math.log(100, 10) → 2
"""

# 📦 Biblioteca random (gera valores aleatórios)
import random

# -------------------------------
# 🎯 Funções principais da random
# -------------------------------

# random.random()
# → Retorna um número float entre 0.0 e 1.0
# Ex: 0.4783

# random.randint(a, b)
# → Retorna um número inteiro entre a e b (inclusive)
# Ex: random.randint(1, 10) → 7

# random.uniform(a, b)
# → Retorna um número float entre a e b
# Ex: random.uniform(1, 10) → 4.7632

# random.choice(lista)
# → Retorna um item aleatório de uma lista (ou tupla, string, etc.)
# Ex: random.choice(['Ana', 'João', 'Carlos'])

# random.choices(lista, k=n)
# → Retorna k elementos aleatórios com repetição
# Ex: random.choices(['A', 'B', 'C'], k=2) → ['B', 'B']

# random.sample(lista, k=n)
# → Retorna k elementos aleatórios SEM repetição
# Ex: random.sample(['A', 'B', 'C'], 2) → ['C', 'A']

# random.shuffle(lista)
# → Embaralha a lista original (modifica a lista)
# Ex:
# nomes = ['Ana', 'Bruno', 'Carla']
# random.shuffle(nomes)
# print(nomes) → ['Carla', 'Ana', 'Bruno'] (ordem pode variar)

