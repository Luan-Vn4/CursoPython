# Aluguel do carro (R$60,00 por dia) e (R$0,15 por km rodado)
dias = float(input("O carro foi alugado por quantos dias?\n"))
vD = 60 * dias
dist = float(input("O carro percorreu quantos quilômetros?\n"))
vKm = (dist * 0.15)
vTotal = vD + vKm

print(f"O carro percorreu {dist}km em {dias} dias\nValor pago: R${vTotal:.2f}")
