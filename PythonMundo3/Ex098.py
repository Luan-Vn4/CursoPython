# Contador
def contador(i=0, f=0, p=1):
    from time import sleep
    if i < f:
        if p < 0:
            p += -1
        for c in range(i, f+1, p):
            sleep(0.3)
            if p == 1:
                if c != f:
                    print(str(c) + '... ', end='')
                else:
                    print(str(c))
            elif p > 1:
                if (c != f-p or (c + p == f)) and c < f:
                    print(str(c) + '... ', end='')
                else:
                    print(str(c))
    else:
        if p > 0:
            p *= -1
        for c in range(i, f-1, p):
            sleep(0.3)
            if p == 1:
                if c != f:
                    print(str(c) + '... ', end='')
                else:
                    print(str(c))
            elif p < 1:
                if (c != f-p or c + p == f) and c > f:
                    print(str(c) + '... ', end='')
                else:
                    print(str(c))


print("Contagem de 1 até 10 de 3 em 3")
contador(1, 10, 3)

print("Contagem de 10 até 0 de 2 em 2")
contador(10, 0, -2)

print("Contagem personalizada!")
ini = int(input("Início: "))
fin = int(input("Final: "))
pas = int(input("Passo: "))
contador(ini, fin, pas)
