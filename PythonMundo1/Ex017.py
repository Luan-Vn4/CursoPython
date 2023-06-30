from math import sqrt
# Hipotenusa do triângulo retângulo
cat1 = float(input("Informe o primeiro cateto: "))
cat2 = float(input("Informe o segundo cateto:"))
hip = sqrt(cat1**2 + cat2**2)
print(f"A hipotenusa de um triângulo retângulo com catetos {cat1} e {cat2} é igual a {hip}")