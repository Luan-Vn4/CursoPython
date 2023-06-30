# Aumento do salário
salario = float(input("Informe o salário do funcionário: R$"))
aumento = float(input("Informe o aumento: %"))/100
nSalario = salario * (1 + aumento)
print(f"Salário atual: R${salario:.2f}\nAumento: %{(aumento * 100):.2f}\nNovo salário: R${nSalario:.2f}")
