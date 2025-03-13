import os

os.system("cls || clear")

# Solicitando dados.
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

# Calcular média.
media = (primeira_nota + segunda_nota) / 2

# Verificando.
if media > 6:
    resultado = "Aprovado."
elif media > 4:
    resultado = "Recuperação."
else:
    resultado = "Reprovado."

# Exibindo dados.
print(f"\nMédia: {media}")
print(f"Resultado: {resultado}")