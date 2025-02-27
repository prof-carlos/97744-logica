# 1 - Limpando o terminal.
import os
os.system("clear")

# 2 - Solicitando dados para o usuário.
print("""
==================== MENU ====================
1   \tDomingo
2   \tSegunda-feira
3   \tTerça-feira
4   \tQuarta-feira
5   \tQuinta-feira
6   \tSexta-feira
7   \tSábado
""")

dia = int(input("Digite um número para o dia da semana: "))

# 3 - Verificando.
if dia > 1 and dia < 7:
    resultado = "Dia útil."
elif dia == 1 or dia == 7:
    resultado = "Fim de semana."
else:
    resultado = "Opção inválida."

# 4 - Exibindo resultados.
print()
print(f"Resultado: {resultado}")