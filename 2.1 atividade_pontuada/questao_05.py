import os

os.system("cls || clear")

# Solicitando dados.
a = int(input("Digite o valor de A: "))
operacao = input("Digite a operação (+ - * / ): ")
b = int(input("Digite o valor de B: "))

match operacao:
    case "+":
        resultado = a + b
    case "-":
        resultado = a - b
    case "*":
        resultado = a * b
    case "/":
        resultado = a / b
    case _:
        print("\nOpção inválida.")
        resultado = 0

print(f"\nResultado: {resultado}")
