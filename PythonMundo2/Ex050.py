# Soma apenas dos números pares
n = []
s = 0
for c in range(0, 6):
    n.append(int(input("Informe um número: ")))
    if n[c] % 2 == 0:
        s = s + n[c]
print(f"A soma dos valores pares da sequência {n} é: {s}")
