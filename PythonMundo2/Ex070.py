# Crie um programa que leia o nome e o preço de vários produtos. (total gasto) (qnts +1000) e (+barato)
produtos, precos, qnt, m1000 = [], [], [], []
total, c = 0, 0
pBarato, barato = 0, ''
resposta = ' '

print("-=-"*7 + "\nMERCADO DO BALACOBACO\n" + "-=-"*7)
while True:
    # Entrada nome do produto
    produtos.append(input("Informe o produto: "))
    # Entrada preço
    while True:
        try:
            precos.append(float(input("Preço: R$")))
            break
        except ValueError as e:
            print("Valor inválido!")
    # Entrada quantidade
    while True:
        try:
            qnt.append(int(input("Quantidade: ")))
            break
        except ValueError as e:
            print("Valor inválido!")

    print("-=-"*8)
    # Verificação
    total += precos[c] * qnt[c]

    if precos[c] > 1000:
        m1000.append(produtos[c])

    if c == 0 or precos[c] < pBarato:
        pBarato = precos[c]
        barato = produtos[c]

    # Continuar ou não
    while resposta not in 'SN':
        resposta = input("Deseja continuar? [S/N]\n").upper().strip()
    if resposta == 'N':
        break
    else:
        c += 1
        resposta = ' '
    print("-=-"*8)

# Resultados
print(f"\nNota fiscal: ")
print("~~~"*14)
for i in range(0, len(produtos)):
    print(f"Produto: {produtos[i]} | Qnt: {qnt[i]} | Preço: R${precos[i]*qnt[i]:.2f}")
print("~~~"*14)
print(f"Total: R${total:.2f}\n")

print(f"Produtos que custaram mais de R$1000,00:")
print("~~~"*14)
for i in range(0, len(m1000)):
    print(m1000[i])
print("~~~"*14)
print(f"Total: {len(m1000)}\n")

print(f"Produto mais barato: {barato} | Preço: R${pBarato:.2f}")
