# Castra nome e peso de pessoas em uma lista (qnts pessoas foram cadastradas) (Pessoas mais pesada) (pessoas mais leves)
# Variáveis
pessoas, maior, menor = [], [], []
nome = ' '
peso = 0

while True:
    # Entrada de variáveis
    nome = input("Nome: ")

    while True:
        try:
            peso = float(input("Peso(kg):"))
            break
        except ValueError as e1:
            print("Valor inválido, tente novamente!")

    # Registra pessoa
    pessoas.append([nome, peso])

    # Verifica continuação
    while True:
        try:
            proc = input("Deseja continuar?")
            if proc not in "SsNn":
                raise ValueError("Resposta inválida!")
            else:
                break
        except ValueError as e1:
            print(str(e1))

    if proc in 'Nn':
        break

# Verificação de peso
for p in pessoas:
    if (not maior) and (not menor):
        maior.append(p[:])
        menor.append(p[:])
    else:
        if p[1] >= maior[0][1]:  # Maior peso
            if p[1] > maior[0][1]:
                maior.clear()
            maior.append(p[:])
        if p[1] <= menor[0][1]:  # Menor peso
            if p[1] < menor[0][1]:
                menor.clear()
            menor.append(p[:])

print(f"{pessoas}\nQuantidade de pessoas cadastradas: {len(pessoas)}")
print(f"Maior peso: {maior[0][1]} | {maior}")
print(f"Menor peso: {menor[0][1]} | {menor}")
