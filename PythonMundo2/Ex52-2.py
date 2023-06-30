num = int(input("Informe um número: "))
c = 2
while num % c != 0:
    c = c + 1
if num == c:
    print(f"O valor {num} é primo")
else:
    print(f"O valor {num} não é primo, pois é divisível por {c}")
