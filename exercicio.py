def exibir_catalogo(filmes):
    print("CATÁLOGO DE FILMES\n")
    print("Nome\n----")
    for filme in filmes:
        print(filme)

filmes = [
    "O Poderoso Chefão",
    "O Senhor dos Anéis: O Retorno do Rei",
    "A Lista de Schindler",
    "Forrest Gump",
    "Titanic",
    "O Rei Leão",
    "Matrix",
    "Interestelar",
    "Cidade de Deus",
    "Parasita"
]

while True:
    print("\n1 - Exibir catálogo")
    print("2 - Sair")

    opcao = input("\nDigite a opção desejada: ")

    if opcao == "1":
        exibir_catalogo(filmes)
    elif opcao == "2":
        print("\nSaindo...")
        break
    else:
        print("\nOpção inválida. Tente novamente.")
