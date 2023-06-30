# Verificar se um número é primo
import itertools
num = int(input("Informe um número: "))
for i in itertools.count(2):
    if num % i == 0:
        break
if num != i:
    print(f"O valor {num} não é primo")
else:
    print(f"O valor {num} é primo")
