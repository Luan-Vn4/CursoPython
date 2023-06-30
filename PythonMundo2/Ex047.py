# Todos os números pares entre determinado intervalo
n1 = int(input("Início: "))
n2 = int(input("Fim: "))
print(f"Números pares entre {n1} e {n2}:")
# Crescente
if n1 < n2:
    for c in range(n1, n2 + 1):
        if c % 2 == 0:
            print(c)
# Decrescente
elif n1 > n2:
    for c in range(n1, n2 - 1, -1):
        if c % 2 == 0:
            print(c)
# Iguais
else:
    if n1 % 2 == 0:
        print("Valores iguais e pares")
    else:
        print("valores iguais e não pares")
