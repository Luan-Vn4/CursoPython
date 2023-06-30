# Determinar se o ano é bissexto
from datetime import date
ano = int(input("Informe um ano: "))
a = date.today().year
print(a)
if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 == 0:
        print(f"{ano} é um ano bissexto!")
    elif ano % 100 == 0 and ano % 400 != 0:
        print(f"{ano} não é bissexto!")
    else:
        print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")
