import os

os.system("cls || clear")

# Solicitando dados.
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

if a == b:
    c = a + b
else: 
    c = a * b

print(f"\nValor da variável C: {c}")
