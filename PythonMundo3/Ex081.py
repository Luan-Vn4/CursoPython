# Ler números, criar lista. Quantos foram digitados, Valores em ordem decrescente e se 5 está na lista
lista, pos5 = [], []
c = 0

while True:
    lista.append(int(input(f"Digite o {c+1}º valor: ")))

    while True:
        resposta = input("Deseja continuar? ")
        if resposta in 'SsNn':
            break
    if resposta in 'Nn':
        break
    else:
        c += 1

print(f"Você digitou {len(lista)} valores")
print(f"Valores em ordem decrescente: {sorted(lista, reverse=True)}")
if 5 in lista:
    print(f"O valor 5 faz parte da lista nas posições")
else:
    print("O valor 5 não faz parte da lista")
