# Cadastro de jogador de futebol com nome e quantidade de gols por partida joga, além do total de gols
gols = {}
jogador = {}
print("-=-"*12)
print(F'{"REGISTRO DE JOGADORES":^36}')
print("-=-"*12)

# Entrada de dados
jogador['nome'] = input("Nome do jogador: ")
qnt = int(input(f"Quantidade de partidas de {jogador['nome']}: "))
print('~'*36)
for c in range(0, qnt):
    gols[f'partida {c+1}'] = int(input(f"Gols na partida {c+1}: "))
    if c == 0:
        jogador['total'] = gols[f'partida {c+1}']
    else:
        jogador['total'] += gols[f'partida {c+1}']
jogador['gols'] = gols.copy()

# Mostra os dados do dicionário
print("-=-"*12)
print(f"{jogador}")
print("-=-"*12)

# Mostra os valores do campo
for k, v in jogador.items():
    if k == 'gols':
        print(f"O campo {k} tem os valores: {', '.join(str(x) for x in jogador[k].values())}")
    else:
        print(f"O campo {k} tem o valor: {v}")
print("-=-"*12)

# Recaptula os gols
print(f"O jogador Joelson jogou {qnt} partida(s)")
for k, v in jogador['gols'].items():
    print(f"Na {k}, fez {v} gols")
print(f"Fiz um total de {jogador['total']} gols")
