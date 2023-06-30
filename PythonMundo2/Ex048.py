# Soma entre todos os números ímpares, múltiplos de 3, entre 1 até 500
s = 0
for c in range(1, 501, 2):
    if (c % 2 != 0) and (c % 3 == 0):
        s = s + c
print(f"A soma dos valores ímpares, múltiplos de três que se encontram entre 1 e 500, incluído, é: {s}")
