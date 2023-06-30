# Aumento de salário (10% para superior a 1250) (15% para inferiores ou iguais a 1250)
sal = float(input("Informe o salário: R$"))
if sal > 1250:
    salN = sal * 1.10
    print(f"O salário de R${sal:.2f} um aumento de 10% e passou a valer: R${salN:.2f}")
else:
    salN = sal*1.15
    print(f"O salário de R${sal:.2f} teve um aumento de 15% e passou a valer: R${salN:.2f}")
