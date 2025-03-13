import os

os.system("cls || clear")

# Solicitando dados.
nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preco do produto: "))
quantidade_produto = float(input("Digite a quantidade do produto: "))

preco_total = quantidade_produto * preco_produto

if quantidade_produto <= 5:
    desconto = preco_total * 0.02
elif quantidade_produto <= 10:
    desconto = preco_total * 0.03
else:
    desconto = preco_total * 0.05

valor_pagar = preco_total - desconto

# Exibindo dados.
print(f"\nPreço sem desconto: {preco_total}")
print(f"Preço com desconto: {valor_pagar}")
