# Desconto
preco = float("{:.2f}".format(float(input("Informe o preço do produto: R$"))))
desconto = float(input("Desconto: %"))/100
precoF = preco * (1 - desconto)
print(f"Preço: R${preco:.2f}\nDesconto: %{desconto*100:.2f}\nPreço Final: R${precoF:.2f}")
