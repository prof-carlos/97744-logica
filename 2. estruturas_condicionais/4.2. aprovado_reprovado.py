import os

os.system("clear")

# Utilizando condicionais aninhadas.
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))

media = (primeira_nota + segunda_nota + terceira_nota) / 3

if media < 7:
    resultado = "Reprovado!"
else:
    resultado = "Aprovado!"

print(f"\nMédia: {media}")
print(f"Resultado: {resultado}")
