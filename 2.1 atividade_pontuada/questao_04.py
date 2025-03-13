import os

os.system("cls || clear")

# Solicitando dados.
quantidade_maca = int(input("Digite a quantidade de maçãs em Kg: "))
quantidade_morango = int(input("Digite a quantidade de morangos em Kg: "))

if quantidade_maca <= 5:
    preco_maca = 1.80
else: 
    preco_maca = 1.50

if quantidade_morango <= 5:
    preco_morango = 2.50
else: 
    preco_morango = 2.20

preco_total_maca = preco_maca * quantidade_maca
preco_total_morango = preco_morango * quantidade_morango

preco_total = preco_total_maca + preco_total_morango
quantidade_total = quantidade_maca + quantidade_morango

if quantidade_total >= 10 or preco_total > 15:
    desconto = preco_total * 0.10 
else:
    desconto = 0

valor_pagar = preco_total - desconto

# Exibindo dados.
print(f"\nPreço total de maçãs: R$ {preco_total_maca:.2f}")
print(f"Preço total de morangos: R$ {preco_total_morango:.2f}")
print(f"Quantidade de morangos e maçãs: {quantidade_total} Kg")
print(f"Preço sem desconto: R$ {preco_total:.2f}")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_pagar:.2f}")