# 1 - Limpando o terminal.
import os
os.system("clear")

# 2 - Solicitando dados para o usuário.
idade = int(input("Digite sua idade: "))

# 3 - Verificando os dados cadastrados com os dados informados pelo usuário.

# OPÇÃO 1.
if idade < 18 or idade > 65:
    print("Não é obrigado a votar!")
else:
    print("É brigado a votar!")

# -------------------------------------

# OPÇÃO 2.
if idade >= 18 and idade <= 65:
    print("É brigado a votar!")
else:
    print("Não é obrigado a votar!")