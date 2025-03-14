import os

os.system("cls || clear")

nota = 0
soma = 0

for i in range(4):
   nota = float(input("Digite uma nota: "))
   soma += nota

media = soma / 4

print()
print(f"Média: {media}")
