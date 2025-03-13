import os

os.system("cls || clear")

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de c: "))

soma = a + b

if soma > c:
    print(f"A soma de A+B é maior que C")
else:
    print(f"A soma de A+B é menor que C")