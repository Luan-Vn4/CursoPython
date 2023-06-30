# Compare dois números inteiros
n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
if n1 > n2:
    print(f"O primeiro número ({n1}) é maior que o segundo ({n2})")
elif n1 < n2:
    print(f"O segundo número ({n2}) é maior que o primeiro ({n1})")
else:
    print(f"Os números ({n1}) e ({n2}) são iguais")
