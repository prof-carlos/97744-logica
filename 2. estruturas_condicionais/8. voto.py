# 1 - Limpando o terminal.
import os
os.system("clear")

# 2 - Solicitando dados para o usuário.
idade = int(input("Digite sua idade: "))

# 3 - Verificando os dados cadastrados com os dados informados pelo usuário.

# OPÇÃO 1.
if idade < 16:
    print("Não pode votar.")
elif idade < 18:
    print("Voto opcional.")
elif idade <= 65:
    print("Voto obrigatório.")
else:
    print("Não é obrigado a votar.")
