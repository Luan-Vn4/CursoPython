# Leia de 0 a 9999 e mostra na tela as unidades separadas
oprt = True
while oprt is True:
    num = int(input("Informe um número de 0 a 9999: "))
    if num in range(9999):
        numStr = str(num)
        if len(numStr) == 1:
            print(f"Unidade: {numStr[0]}")
            oprt = False
        elif len(numStr) == 2:
            print(f"Unidade: {numStr[1]}")
            print(f"Dezena: {numStr[0]}")
            oprt = False
        elif len(numStr) == 3:
            print(f"Unidade: {numStr[2]}")
            print(f"Dezena: {numStr[1]}")
            print(f"Centena: {numStr[0]}")
            oprt = False
        else:
            print(f"Unidade: {numStr[3]}")
            print(f"Dezena: {numStr[2]}")
            print(f"Centena: {numStr[1]}")
            print(f"Milhar: {numStr[0]}")
            oprt = False
    else:
        print("Número inválido, tente novamente!")