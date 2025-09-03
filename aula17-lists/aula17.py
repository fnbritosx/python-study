# 📌 RESUMO DE LISTAS EM PYTHON

# ✅ CRIAÇÃO DE LISTA
lista = [1, 2, 3, 'python', True]

# ✅ ACESSANDO ELEMENTOS (por índice)
lista[0]       # Primeiro elemento
lista[-1]      # Último elemento

# ✅ FATIAMENTO
lista[1:3]     # Do índice 1 ao 2
lista[:3]      # Do início ao índice 2
lista[2:]      # Do índice 2 até o fim

# ✅ MODIFICANDO VALORES
lista[0] = 100

# ✅ ADICIONANDO ELEMENTOS
lista.append('novo')      # Adiciona no final
lista.insert(2, 'item')   # Insere na posição 2
lista.extend([4, 5])      # Adiciona vários itens

# ✅ REMOVENDO ELEMENTOS
lista.remove('python')    # Remove o valor (se existir)
del lista[1]              # Remove pelo índice
item = lista.pop()        # Remove e retorna o último

# ✅ OUTROS MÉTODOS ÚTEIS
len(lista)                # Tamanho da lista
lista.sort()              # Ordena (números ou strings)
lista.reverse()           # Inverte a ordem
lista.count(2)            # Conta quantas vezes aparece o valor 2
lista.index(100)          # Retorna o índice do valor 100

# ✅ PERCORRER LISTA
for item in lista:
    print(item)

# ✅ LISTAS ANINHADAS
matriz = [[1, 2], [3, 4]]
print(matriz[0][1])  # Acessa o valor 2

# ✅ COPIAR LISTAS (cópia verdadeira)
copia = lista[:]         # Cópia independente
