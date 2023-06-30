# Adivinhar o número do computador
from random import randint
import time
n1 = randint(0, 5)
print("-=-"*12)
n2 = int(input("Tente adivinhar um número de 0 a 5:\n" + "-=-"*12 + "\n"))

print("Processando...")
time.sleep(3)

if n2 == n1:
    print(f"Parabéns!! Você acertou o número {n1}")
else:
    print(f"Mais sorte na próxima =(\nO número era {n1}")
