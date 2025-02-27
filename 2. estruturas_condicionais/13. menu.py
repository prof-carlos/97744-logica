# 1 - Limpando o terminal.
import os
os.system("clear")

# 2 - Solicitando dados para o usuário.
print("""
==================== MENU ====================
Código  \tPrato     \t\tValor
1   \t\tPicanha   \t\t25,00
2   \t\tLasanha   \t\t20,00
3   \t\tStrogonoff   \t\t18,00
4   \t\tBife acebolado   \t15,00
5   \t\tPão com ovo   \t\t5,00
""")

opcao = int(input("Digite a opção desejada: "))

# 3 - Verificando.
match opcao:
    case 1:
        prato = "Picanha"
        valor = 25
    case 2:
        prato = "Lasanha"
        valor = 20
    case 3:
        prato = "Strogonoff"
        valor = 18
    case 4:
        prato = "Bife acebolado"
        valor = 15
    case 5:
        prato = "Pão com ovo"
        valor = 5
    case _:
        prato = "Opção inválida"
        valor = 0

# 4 - Exibindo resultados.
print()
print(f"Prato: {prato}")
print(f"Valor: R$ {valor:.2f}")