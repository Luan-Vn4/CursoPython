# Menu / ler dois números / somar / multiplica / maior / novos números / sair
n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
while True:
    r = int(input("[1]Somar [2]Multiplicar [3]Maior [4]Novos números [5]Sair\n"))
    match r:
        case 1:
            print(f"A soma de {n1} e {n2} é: {n1 + n2}\n")
        case 2:
            print(f"O produto entre {n1} e {n2} é: {n1 * n2}\n")
        case 3:
            if n1 > n2:
                print(f"{n1} é o maior número\n")
            elif n2 > n1:
                print(f"{n2} é o maior número\n")
            else:
                print("Os números são iguais\n")
        case 4:
            n1 = int(input("Informe o primeiro número: "))
            n2 = int(input("Informe o segundo número: "))
            print('\n')
        case 5:
            break
        case _:
            print("Resposta inválida! Tente novamente\n")
