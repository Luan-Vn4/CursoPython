# Sequência Fibonaci com FOR
pos = int(input("Deseja vizualizar a sequência fibonacci até qual posição?\n"))
a = 0
b = 1
seq = ''

for c in range(1, pos + 1):
    if c < pos:
        seq += str(b) + ' -> '
    else:
        seq += str(b)
    a, b = b, a+b
print(f"{seq}")
