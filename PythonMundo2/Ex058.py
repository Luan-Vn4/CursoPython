# Adivinhar o número do computador (2.0)
from random import randint
import time

n2 = -1
c = 1

while True:
    n1 = randint(0, 10)
    print("-=-"*12)
    n2 = int(input("Tente adivinhar um número de 0 a 10:\n" + "-=-"*12 + "\n"))

    print("Processando...")
    time.sleep(1)

    if n2 == n1:
        print(f"Parabéns!! Você acertou o número {n1}")
        if c == 1:
            print("Foi necessária apenas uma tentativa!")
        else:
            print(f"Foram necessárias {c} tentativas")
        break
    else:
        print(f"Tente novamente... =(\nO número era {n1}")
        c += 1
