# Criar uma única lista separando pares e ímpares
num = [[], []]

for c in range(0, 7):
    while True:
        try:
            v = int(input(f"Informe o {c+1}º número: "))
            break
        except ValueError as e1:
            print("Valor inválido!")

    if v % 2 == 0:
        num[0].append(v)
    else:
        num[1].append(v)

print(f"Pares: {sorted(num[0])}")
print(f"Ímpares: {sorted(num[1])}")
