# 1 - Limpando o terminal.
import os
os.system("clear")

# 2 - Solicitando dados para o usuário.
primeiro_numero = int(input("Digite o primeiro número: "))
operacao = input("Digite a operação desejada: ")
segundo_numero = int(input("Digite o segundo número: "))

# 3 - Verificando.
match operacao:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero
    case _:
        resultado = "Opção inválida."

# 4 - Exibindo resultados.
print()    
print(f"Primeiro número: {primeiro_numero}")
print(f"Operação: {operacao}")
print(f"Segundo número: {segundo_numero}")
print(f"Resultado: {resultado}")
