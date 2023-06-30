# 4 jogadores jogam um dado; maior número vence; dicionário em ordem
from time import sleep
from random import randint
jogadas = {'p1': 0, 'p2': 0, 'p3': 0, 'p4': 0}
# Definição dos números
for j in jogadas:
    while True:
        n = randint(0, 6)
        if n not in jogadas.values():
            jogadas[j] = n
            break

# Mostra as jogadas
for nome, num in jogadas.items():
    sleep(0.21)
    print(f"{nome} jogou {num}")

# Ordena os jogadores, de acordo com o número jogado(orderna pelos valores)
ranking = dict(sorted(jogadas.items(), key=lambda value: value[1], reverse=True))
print(ranking)
print("Ranking:")
c = 1
for i, v in ranking.items():
    print(f"{c}º lugar: {i} com {v}")
    c += 1