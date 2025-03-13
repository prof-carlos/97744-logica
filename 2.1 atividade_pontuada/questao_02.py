import os

os.system("cls || clear")

# Solicitando dados.
nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo: ").lower()
estado_civil = input("Digite seu estado civil: ").lower()

if sexo == "f" and estado_civil == "casada":
    tempo_de_casada = int(input("Digite o tempo de casada: "))

# Exibindo dados.
print()
print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estado_civil}")
if sexo == "f" and estado_civil == "casada":
    print(f"Tempo de casamento: {tempo_de_casada}")
