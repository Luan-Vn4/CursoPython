# Registrar números sem repetição
lista = []
c = valor = 0
while True:
    while True:
        valor = int(input(f"Informe o {c+1}º valor: "))
        if valor not in lista:
            lista.append(valor)
            break
        else:
            print(f"O valor {valor} já foi dito anteriormente")

    while True:
        resposta = input("Deseja continuar? [S/N]")
        if resposta in 'SsNn':
            break
    if resposta in 'Nn':
        break
    else:
        c += 1

print(f"Os valores digitados foram: {sorted(lista)}")
