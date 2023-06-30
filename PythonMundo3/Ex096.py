# Exercício 93 melhorado
from time import sleep

jogadores = []
gols = {}
jogador = {}
c = 1

print("-=-" * 12)
print(F'{"REGISTRO DE JOGADORES":^36}')
print("-=-" * 12)

while True:
    # Entrada de dados
    jogador['nome'] = input(f"Nome do jogador {c}: ")
    qnt = int(input(f"Quantidade de partidades de {jogador['nome']}: "))
    print('~'*36)
    for c in range(0, qnt):
        gols[f'partida {c+1}'] = int(input(f"Gols na partida {c+1}: "))
        if c == 0:
            jogador['total'] = gols[f'partida {c+1}']
        else:
            jogador['total'] += gols[f'partida {c+1}']
    jogador['gols'] = gols.copy()

    # Cadastro do jogador
    jogadores.append(jogador.copy())

    # Pergunta se deseja continuar
    proc = ' '
    while proc not in 'SsNn':
        proc = input("Deseja continuar? [S/N]")
    if proc in 'Nn':
        break
    else:
        c += 1
        jogador.clear()
        gols.clear()

# Mostra os dados recolhidos em tabela
print(f"{'-=-'*10}")
print(f"{'BANCO DE DADOS':^30}")
print(f"{'-=-'*10}")
print(f"{'Nome':<20}|{'Gols':^12}|{'Total':^8}")
print('-'*43)
for i in jogadores:
    nome = i['nome']
    gols = ', '.join(str(x) for x in i['gols'].values())
    total = i['total']
    print(f"{nome:<20}|{('[' + gols + ']'):^12}|{total:^7}")
print('-'*43)
resp = 0
while resp != 999:
    resp = int(input("Mostrar dados de qual jogador? (999 encerra)"))
    if resp != 999 and 0 < resp <= len(jogadores):
        print('-' * 43)
        print(f"Aproveitamento do jogador: {jogadores[resp-1]['nome']}:")
        for k, v in jogadores[resp-1]['gols'].items():
            print(f"Na {k} fez {v} gols")
        print('-' * 43)

# Encerramento
print("\033[031mEncerrando", end='')
for c in range(0, 3):
    sleep(0.5)
    print(".", end='')
