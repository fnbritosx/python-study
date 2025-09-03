# 🧠 MANIPULAÇÃO DE STRINGS EM PYTHON

# Texto base
texto = "Curso em Vídeo Python"

# ================================
# 🔍 ANÁLISE DE STRINGS
# ================================

print("Análise de Strings:")
print("Tamanho da string:", len(texto))                 # Conta caracteres
print("Quantidade de 'o':", texto.count('o'))           # Conta letras 'o'
print("Posição da palavra 'Vídeo':", texto.find('Vídeo'))  # Encontra palavra
print("A palavra 'Python' está no texto?", 'Python' in texto)  # Verificação com 'in'
print()  # linha em branco

# ================================
# 🔄 TRANSFORMAÇÃO DE STRINGS
# ================================

print("Transformações de Strings:")
print("Substituindo 'Python' por 'Java':", texto.replace('Python', 'Java'))
print("Tudo em maiúsculas:", texto.upper())
print("Tudo em minúsculas:", texto.lower())
print("Capitalizado (só primeira letra maiúscula):", texto.capitalize())
print("Título (cada palavra com inicial maiúscula):", texto.title())
print("Removendo espaços dos dois lados:", texto.strip())
print("Removendo espaços da direita:", texto.rstrip())
print("Removendo espaços da esquerda:", texto.lstrip())
print()

# ================================
# 🔗 DIVISÃO E JUNÇÃO DE STRINGS
# ================================

print("Divisão e Junção de Strings:")
palavras = texto.split()   # Divide a frase em palavras
print("Lista de palavras:", palavras)
print("Palavras unidas com '-':", '-'.join(palavras))
print()

# ================================
# 🔢 FATIAMENTO DE STRINGS
# ================================

print("Fatiamento de Strings:")
print("Primeiros 5 caracteres:", texto[0:5])
print("Caracteres de 6 a 8:", texto[6:8])
print("Palavra 'Vídeo':", texto[9:14])
print("Do início até 5:", texto[:5])
print("Do 15 até o fim:", texto[15:])
print("Texto de 2 em 2 caracteres:", texto[::2])
