import os
import time

os.system("cls || clear")

print("Contagem de 2 em 2.")
for i in range(1, 11, 2):
    print(f"Valor da variável i: {i}")
    time.sleep(1) # espera 1 segundo

print("ACABOU.")