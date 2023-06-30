# Dobro do preço/ Metade do preço/ % de aumento/ % de desconto/ resumo/ formatar
def dobrar(din, formated=False):
    if formated:
        return formatar(din * 2)
    else:
        return din * 2


def metade(din, formated=False):
    if formated:
        return formatar(din/2)
    else:
        return din/2


def aumento(din, porc, formated=False):
    if formated:
        return formatar(din * (1+(porc/100)))
    else:
        return din * (1+(porc/100))


def desconto(din, porc, formated=False):
    if formated:
        return formatar(din * (1-(porc/100)))
    else:
        return din * (1-(porc/100))


def formatar(num):
    return f'R${num:.2f}'


def resumo(num, aum, desc):
    print("-=-"*10)
    print(f"{'Preço analisado:':<20}{formatar(num):<12}")
    print(f"{'Dobro do preço:':<20}{dobrar(num, formated=True):<12}")
    print(f"{f'{aum}% de aumento:':<20}{aumento(num, aum, formated=True):<12}")
    print(f"{f'{desc}% de desconto:':<20}{desconto(num, desc, formated=True):<12}")
    print("-=-"*10)


resumo(1000, 100, 50)
