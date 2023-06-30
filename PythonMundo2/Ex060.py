# Fatorial
num = int(input("Informe um número: "))
fat = 1
c = 0
oprt = ''

if num == 0:
    fac = 1
else:
    while c != num:
        fat *= (num - c)
        if (num - c > 1):
            oprt += str(num - c) + 'x'
        else:
            oprt += str(num - c)
        c += 1
if num != 0:
    print(f"{num}! = " + oprt + f" = {fat}")
else:
    print(f"{num}! = {fat}")
