from UtilidadesEx112 import dados, moeda
valor = dados.input_coin("Informe o valor: R$")
desc = dados.input_coin("Porcentagem de desconto: ")
aum = dados.input_coin("Porcentagem de aumento: ")

print(f"O dobro de {moeda.formatar(valor)} é {moeda.dobrar(valor, formated=True)}")
print(f"A metade de {moeda.formatar(valor)} é {moeda.metade(valor, formated=True)}")
print(f"Aumentando {aum}%, temos: {moeda.aumento(valor, aum, formated=True)}")
print(f"Descontando {desc}%, temos: {moeda.desconto(valor, desc, formated=True)}")
print('\n'*2)
moeda.resumo(valor, aum, desc)
