# Preço do produto (10% de desconto à vista ou 5% no cartão) (2x preço normal) (3x ou mais 20% de juros)
menu = ("-=-" * 10)
# Entrada do preço
prec = float(input("Preço do produto: R$"))
# Forma de pagamento
print(f'Valor: R${prec:.2f}')  # Display do valor
resp = int(input("Forma de pagamento: [1]À vista [2]Parcelado\n"))
match resp:
    case 1:  # À VISTA
        resp = int(input("[1]Cartão [2]Dinheiro ou cheque\n"))
        match resp:
            case 1:
                precF = prec * 0.95
                print(menu)
                print(f"Valor original: R${prec:.2f}\nDesconto: 5%\nValor final: R${precF:.2f}")
                print(menu)
            case 2:
                precF = prec * 0.90
                print(menu)
                print(f"Valor original: R${prec:.2f}\nDesconto: 10%\nValor final: R${precF:.2f}")
                print(menu)
    case 2:  # PARCELADO
        print("Juros de 20% a partir de 3 parcelas")
        qt = int(input("Quantidade de parcelas: "))
        if qt <= 2:
            vParc = prec / qt
            print(menu)
            print(f"Valor: R${prec:.2f}\n{qt} parcelas de R${vParc:.2f}")
            print(menu)
        else:
            precF = prec * 1.20
            vParc = precF / qt
            print(menu)
            print(f"Valor original: R${prec:.2f}\nJuros: 20%\nValor final: R${precF:.2f}\n{qt} parcelas de "
                  f"R${vParc:.2f}")
            print(menu)
