# Sortear n jogos da Mega Sena
from random import randint
from time import sleep
jogos = []
print("-"*30)
print(f"{'JOGO NA MEGA SENA':^30}")
print("-"*30)
v = int(input("Quantidade de jogos a sortear: "))
print("~"*30)

for jogo in range(0, v):
    jogos.append([])  # Cria a lista(jogo) dentro da lista de jogos
    for num in range(0, 6):  # Adiciona os 6 números do jogo criado
        while True:
            n = randint(0, 60)
            if n not in jogos[jogo]:  # Verifica se o valor já foi escolhido
                jogos[jogo].append(n)
                break
        jogos[jogo].sort()

print(f"Os {v} jogos sorteados foram:")
for c in range(0, len(jogos)):
    sleep(0.21)
    print(f"Jogo {c+1}: {jogos[c]}")
