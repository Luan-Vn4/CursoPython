# Ler 4 valores, salvar na tupla e mostrar qnt 9, posição do primeiro 3 e quais os números pares
n1 = int(input("Informe o primeiro valor: "))
n2 = int(input("Informe o segundo valor: "))
n3 = int(input("Informe o terceiro valor: "))
n4 = int(input("Informe o quarto valor: "))
num = (n1, n2, n3, n4)

pares = []
for c in num:
    if c % 2 == 0:
        pares.append(c)

print(f"{sorted(num)}")
print(f"O número 9 apareceu {num.count(9)}")
if 3 in num:
    print(f"O primeiro 3 aparece na posição {num.index(3) + 1}")
else:
    print(f"O número 3 não aparece em nenhuma posição")
print(f"Há {len(pares)} números pares que são: {sorted(pares)}")
