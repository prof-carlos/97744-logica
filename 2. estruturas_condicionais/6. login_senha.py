# 1 - Limpando o terminal.
import os
os.system("clear")

# 2 - Cadastrando o login e senha.
login_cadastrado = "aluno"
senha_cadastrada = "123"

# 3 - Solicitando dados para o usuário.
login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

# 4 - Verificando os dados cadastrados com os dados informados
# pelo usuário.
if login_cadastrado == login and senha_cadastrada == senha:
    print("Bem-vindo!")
else:
    print("Login ou senha inválidos!")