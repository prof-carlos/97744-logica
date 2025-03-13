import os

os.system("cls || clear")

# Solicitando dados.
valor_solicitado = float(input("Digite o valor de empréstimo desejado: "))
renda_mensal = float(input("Digite o valor da sua renda mensal: "))
quantidade_parcelas = float(input("Digite a quantidade de parcelas que pretende pagar: "))

valor_maximo_emprestimo = renda_mensal * 10
valor_maximo_prestacao = renda_mensal * 0.30
valor_por_parcela = valor_solicitado / quantidade_parcelas

if valor_solicitado <= valor_maximo_emprestimo and valor_por_parcela <= valor_maximo_prestacao:
    resultado = "Autorizado."
else:
    resultado = "Negado."

# Exibindo dados.
print(f"Resultado: {resultado}")
