# Cadastrar pessoas e verificar quantas são maiores, quantos homens e quantas mulheres com menos de 20 anos
idade = []
sexo = []
maioridade = 0
homens = 0
mu20 = 0
c = 0

while True:
    # Pergunta idade
    while True:
        try:
            idade.append(int(input(f"Informe a {c+1}º idade: ")))
            break
        except ValueError as error:
            print("Digite um número inteiro")
            print(error)

    # Pergunta sexo
    sexo.append(input(f"Informe o {c + 1}º sexo: "))
    while sexo[c] not in 'MF':
        sexo.__setitem__(c, input(f"Informe o {c + 1}º sexo: "))

    if idade[c] >= 18:
        maioridade += 1
    if sexo[c] == 'M':
        homens += 1
    if sexo[c] == 'F' and idade[c] < 20:
        mu20 += 1
    c += 1

    while True:
        resposta = input("Deseja continuar? [S/N]")
        if resposta in 'SsNn':
            break
    if resposta in 'Nn':
        break

print(f"Pessoas com mais de 18 anos: {maioridade}\nNúmero de homens: {homens}\nMulheres com menos de 20 anos: {mu20}")
