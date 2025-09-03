# DICIONÁRIO EM PYTHON - RESUMO SIMPLES

# Um dicionário armazena dados em pares: CHAVE → VALOR
# Exemplo: pessoa = {"nome": "Ana", "idade": 25}

# • A CHAVE (key) funciona como um "índice personalizado"
#   - Em vez de usar números como nas listas (ex: lista[0]),
#     usamos nomes ou identificadores (ex: pessoa["nome"])

# • O VALOR (value) é o dado associado à chave
#   - Pode ser número, texto, lista, outro dicionário, etc.

# Principais funções e comandos:
# dicionario.keys()      → retorna todas as chaves
# dicionario.values()    → retorna todos os valores
# dicionario.items()     → retorna os pares chave-valor
# dicionario.get("chave") → retorna o valor (evita erro se não existir)
# dicionario["chave"]    → acessa diretamente o valor da chave
# dicionario["nova"] = x → adiciona ou modifica chave
# del dicionario["chave"] → remove a chave

# Exemplo:
# aluno = {"nome": "Lucas", "nota": 8.5}
# print(aluno["nome"])     # Mostra "Lucas"
# print(aluno.get("turma")) # Retorna None (não dá erro)

# Também é possível fazer lista de dicionários:
# turma = [{"nome": "Ana"}, {"nome": "Pedro"}]
