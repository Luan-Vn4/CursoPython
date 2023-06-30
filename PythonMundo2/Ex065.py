# Ler vários números, mostrar a média, maior e menor valor e depois perguntar se quer continuar
num, soma, c = 1, 0, 0
maior, menor = 0, 0
while True:
    while num != 0:
        num = int(input("Digite um número (0 encerra): "))
        if num != 0:
            if num > maior:
                maior = num
            if c == 0:
                menor = num
            elif num < menor:
                menor = num
            soma += num
            c += 1
    print(f"A média dos números é: {soma/c}\nMenor: {menor}\nMaior: {maior}\n")
    resposta = input("Deseja continuar? [S/N]").upper().strip()
    if resposta == 'N':
        print("\033[31mPrograma encerrado!")
        break
    else:
        num = 1
