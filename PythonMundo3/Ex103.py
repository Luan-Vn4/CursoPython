# Função que registra jogador
def registrar(nome, gols=0):
    if nome == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {gols} gols no campeonato!'


nome_jogador = input("Nome: ")
try:
    gols_jogador = int(input("Gols: "))
except ValueError as e1:
    gols_jogador = 0

print(registrar(nome_jogador, gols_jogador))
