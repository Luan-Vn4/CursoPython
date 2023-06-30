# Pedra, papel ou tesoura
from time import sleep
from random import randint

jogador = int(input("[1]Pedra [2]Papel [3]Tesoura\n"))
comp = randint(1, 3)
print("Processando...")
sleep(3)

# Atribuição da resposta
match comp:
    case 1:
        resp = 'Pedra'
    case 2:
        resp = 'Papel'
    case 3:
        resp = 'Tesoura'

# Resultados
if comp == jogador:
    print(f"Empate!! O computador também escolheu {resp}")

elif comp == 1:
    if jogador == 2:
        print(f"Parabéns, você ganhou!! O computador escolheu {resp}")
    else:
        print(f"Você perdeu =(\nO computador escolheu {resp}")

elif comp == 2:
    if jogador == 3:
        print(f"Parabéns, você ganhou!! O computador escolheu {resp}")
    else:
        print(f"Você perdeu =(\nO computador escolheu {resp}")

elif comp == 3:
    if jogador == 1:
        print(f"Parabéns, você ganhou!! O computador escolheu {resp}")
    else:
        print(f"Você perdeu =(\nO computador escolheu {resp}")
