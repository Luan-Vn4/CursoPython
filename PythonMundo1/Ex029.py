# Ler velocidade e multar acima de 80km/h
v = float(input("Informe a velocidade: "))
if v > 80:
    multa = (v-80) * 7
    print(f"Acima de 80km/h!! Multa: {multa:.2f}")
else:
    print("Velocidade dentro do limite")
