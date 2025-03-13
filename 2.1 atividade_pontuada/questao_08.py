import os

os.system("cls || clear")

# Solicitando dados.
cor = input("Digite a cor do CD: ").lower()

match cor:
    case "verde":
        preco = 10
    case "azul":
        preco = 20
    case "amarelo":
        preco = 40
    case "vermelho":
        preco = 50
    case _:
        print("\nOpção inválida.")
        preco = 0

# Exibindo dados.
print(f"Preço: {preco}")
