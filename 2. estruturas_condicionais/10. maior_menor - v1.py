# 1 - Limpando o terminal.
import os
os.system("clear")

# 2 - Solicitando dados para o usuário.
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
terceiro_numero = int(input("Digite o terceiro número: "))

# 3 - Verificando o maior e o menor.
if (primeiro_numero > segundo_numero) and (primeiro_numero > terceiro_numero):
    maior = primeiro_numero
elif segundo_numero < terceiro_numero:    
    menor = segundo_numero
else:
    menor = terceiro_numero

if (segundo_numero > primeiro_numero) and (segundo_numero > terceiro_numero):
    maior = segundo_numero
elif primeiro_numero < terceiro_numero:    
    menor = primeiro_numero
else:
    menor = terceiro_numero

if (terceiro_numero > primeiro_numero) and (terceiro_numero > segundo_numero):
    maior = terceiro_numero
elif primeiro_numero < segundo_numero:
    menor = primeiro_numero
else:
    menor = segundo_numero

# 4 - Exibindo resultados.
print()    
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")