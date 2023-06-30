# 0.50 até 200km e 0.45 em viagens mais longas. Calcular preço
dist = float(input("Informe a distãncia da viagem(km): "))
if dist <= 200:
    prec = dist * 0.50
    print(f"O valor a ser pago é: {prec:.2f}")
else:
    prec = dist * 0.45
    print(f"O valor a ser pago é: {prec:.2f}")
