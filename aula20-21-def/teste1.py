def cadastrar_usuario(**dados):
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")

cadastrar_usuario(nome="Ana", idade=30, email="ana@gmail.com")

