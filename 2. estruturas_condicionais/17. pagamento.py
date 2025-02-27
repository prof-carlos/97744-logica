# 1 - Limpando o terminal.
import os
os.system("clear")

# 2 - Solicitando dados para o usuário.
valor_produto = float(input("Digite o valor do produto: "))

print("""
==================== FORMA DE PAGAMETNO ====================
1   \tÁ vista
2   \tÁ prazo
""")
forma_de_pagamento = int(input("Digite a forma de pagamento: "))

# 3 - Verificando.
match forma_de_pagamento:
    case 1: 
        # Obtendo o valor do desconto de 10%.
        desconto = valor_produto * 0.10
        
    case 2: 
        parcelas = int(input("Digite a quantidade de parcelas: "))
        
    case _:
        print("Opção inválida.")

# 4 - Exibindo resultados.
print()