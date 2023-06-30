# Pergunta valor da casa, salário e quantos anos vai pagar
# Prestação mensal não pode exceder 30% ou o empréstimo será negado
prec = float(input("Informe o valor da casa: R$"))
sal = float(input("Informe seu salário: R$"))
temp = int(input("Em quanto tempo pretende pagar a casa? (anos)\n"))

prestM = (prec/temp)/12

if prestM <= sal * 0.30:
    print(f"Parabéns! A prestação mensal será de R${prestM:.2f} por {temp} anos.")
else:
    print("Infelizmente seu empréstimo foi negado\nO valor da prestação excede 30% do salário")