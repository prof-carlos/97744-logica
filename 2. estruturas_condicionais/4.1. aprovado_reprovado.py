import os

os.system("clear")

# Utilizando condicionais aninhadas.
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))

media = (primeira_nota + segunda_nota + terceira_nota) / 3

print()
print(f"Média: {media}")

if media < 7:
    print("Reprovado!")
else:
    print("Aprovado!")

