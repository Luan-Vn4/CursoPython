# Tabuada
n = int(input("Informe um número: "))

contador = 0
while contador < 11:
    t = n * contador
    print(f"{n} * {contador} = {t}")
    contador = contador + 1

print("\nConcluído")
