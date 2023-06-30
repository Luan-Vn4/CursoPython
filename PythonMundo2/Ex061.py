# Progressão aritmética com while
pa = ''  # String que contém a progressão
resp = 0  # Termos a mais dos 10 iniciais
pos = 10  # Posição que a PA termina

i = int(input("Informe o primeiro termo da progressão aritmética: "))
n = i  # enéssimo termo que será somado a string
r = int(input("Razão: "))

while True:
    pos += resp  # Adiciona os termos a mais na posição em que a PA termina

    while n <= i + (pos - 1) * r:
        if n < i + (pos - 1) * r:
            pa += str(n) + ' -> '
        else:
            pa += str(n)
        n += r

    print("Progressão aritmética:")
    print(f"{pa}")

    resp = int(input("Quantos termos você quer ver a mais? (0 encerra)\n"))
    if resp <= 0:
        print("\033[031mPrograma encerrado!")
        break
    else:
        pa += ' -> '
