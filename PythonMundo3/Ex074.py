# Tupla com 5 números aleatórios mostrando o menor e o maior valor
from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), (randint(0, 10)))
maior = 0
menor = num[0]
for c in num:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print(num)
print(f"Maior número: {max(num)}\nMenor número: {min(num)}")
print(f"Maior número: {maior}\nMenor número: {menor}")
