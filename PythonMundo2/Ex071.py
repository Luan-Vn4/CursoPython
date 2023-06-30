# Sacar dinheiro (notas de 50, 20, 10 e 1)
sobra = valor = n50 = n20 = n10 = n1 = 0
q1, q10, q20, q50 = 0, 0, 10, 10
oprt = True

print("=="*8 + "\nBanco do Brasil\n" + "=="*8)
print(f"Cédulas disponíveis:\n[R$50,  R$20,  R$10,  R)$1]")
print(f"[({q50}) | ({q20}) | ({q10}) | ({q1})]")
while True:
    try:
        valor = int(input("Digite o valor que deseja sacar: R$"))
        break
    except ValueError as error:
        print("Valor inválido!")

# Contador de cédulas
while True:
    # Verificação 50
    if valor >= 50:
        n50 = valor // 50  # Verifica a quantidade de notas necessárias
        if n50 > q50:  # Se a quantidade necessária for maior que a disponível, a quantidade emitida é o disponível
            n50 = q50
        valor = valor - (n50 * 50)  # Desconta o valor de acordo com a quantidade de notas emitidas
        q50 -= n50  # Retira a quantidade de notas emitidas
        if valor == 0:
            break

    # Verificação 20
    if valor >= 20:
        n20 = valor//20
        if n20 > q20:
            n20 = q20
        valor = valor - (n20 * 20)
        q20 -= n20
        if valor == 0:
            break

    # Verificação 10
    if valor >= 10:
        n10 = valor//10
        if n10 > q10:
            n10 = q10
        valor = valor - (n10 * 10)
        q10 -= n10
        if valor == 0:
            break

    # Verificação 1
    if valor >= 1:
        n1 = valor
        if n1 > q1:
            oprt = False
        break

if oprt is True:
    if n50 > 0:
        print(f"Total de {n50} cédulas de R$50")
    if n20 > 0:
        print(f"Total de {n20} cédulas de R$20")
    if n10 > 0:
        print(f"Total de {n10} cédulas de R$10")
    if n1 > 0:
        print(f"Total de {n1} moedas de R$1")
else:
    print("Não há moedas/cédulas suficiente =(")
