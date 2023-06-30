# Programa de par ou ímpar
from random import randint
from time import sleep
vermelho = '\033[031m'
verde = '\033[032m'
normal = '\033[m'
menu, resultLine = '-=-' * 10, '~~~' * 10
totVit = 0

while True:
    print(menu)
    escolha = int(input(f"Ímpar(1) ou Par[2]\n{menu}\n"))
    print(menu)
    jogada = int(input(f"Número entre 0 e 10:\n{menu}\n "))
    computador = randint(0, 10)
    soma = jogada + computador

    print(resultLine)
    for c in range(1, 4):
        sleep(1)
        print(f"{c}... ", end='')
    sleep(1)
    print("Vamos arrastar!!!")
    print(f"Jogador: {jogada}\nComputador: {computador}")

    sleep(6)
    print(resultLine)
    match escolha:
        case 1:
            if soma % 2 == 0:
                print(vermelho + f"Você perdeu! {soma} é par =(" + normal)
                print(f'Total de vitórias: {totVit}')
                break
            else:
                print(vermelho + f"Você ganhou! {soma} é ímpar" + normal)
                totVit += 1
        case 2:
            if soma % 2 == 0:
                print(verde + f"Você ganhou! {soma} é par" + normal)
                totVit += 1
            else:
                print(vermelho + f"Você perdeu! {soma} é ímpar =(" + normal)
                print(f'Total de vitórias: {totVit}')
                break
