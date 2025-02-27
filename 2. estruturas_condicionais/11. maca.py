# 1 - Limpando o terminal.
import os
os.system("clear")

# 2 - Solicitando dados para o usuário.
quantidade_maca = int(input("Digite a quantidade de maçã desejada: "))

# 3 - Verificando.
if quantidade_maca < 12:
    preco_maca = 1.30
else: 
    preco_maca = 1.00

valor_total = quantidade_maca * preco_maca

# 4 - Exibindo resultados.
print()    
print(f"Valor total da compra R$ {valor_total:.2f}")
