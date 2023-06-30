# Ler primeiro termo e razão de uma PA (mostrar 10 primeiros termos)
i = int(input("Informe o primeiro termo da progressão aritmética: "))
r = int(input("Razão: "))
s = ''
for c in range(0, 10):
    if c < 9:
        s = s + str(i) + ', '
    else:
        s = s + str(i)
    i = i + r
print(s)
