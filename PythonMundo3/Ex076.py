# Produtos e preços tabela
produtos = ('Lápis', "Borracha", "Caderno", "Estojo", "Transferidor", "Compasso", "Mochila", "Canetas", "Livro")
precos = ('1.75', '2.00', '15.90', '25.00', '4.20', '9.99', '120.32', '22.30', '34.90')

print("-" * 35)
print(f"{'LISTAGEM DE PREÇOS': ^35}")
print("-" * 35)

for c in range(len(produtos)):
    print(f"{produtos[c]:.<24}" + f"R${precos[c]: >8}")
print('-' * 35)