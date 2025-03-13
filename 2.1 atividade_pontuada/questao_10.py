import os

os.system("cls || clear")

# Solicitando dados.
preco_alcool = 3.79
preco_gasolina = 6.59

tipo_combustivel = input(f"A - Álcool - {preco_alcool}\nG - Gasolina - {preco_gasolina}\nDigite o tipo de combustível : ").upper()
quantidade_litros = float(input("Digite a quantidade de combustível: "))


match tipo_combustivel:
    case "A":
        if quantidade_litros <= 25:
            desconto = preco_alcool * 0.02
        else:
            desconto = preco_alcool * 0.04
        preco_por_litro = preco_alcool - desconto
    case "G":
        if quantidade_litros <= 25:
            desconto = preco_gasolina * 0.03
        else:
            desconto = preco_gasolina * 0.05
        preco_por_litro = preco_gasolina - desconto
    case _:
        print("\nOpção inválida.")
        preco_por_litro = 0

valor_pagar = quantidade_litros * preco_por_litro

# Exibindo dados.
print(f"\nPreço por litro: {preco_por_litro:.2f}")
print(f"Total a pagar: {valor_pagar:.2f}")        
        
