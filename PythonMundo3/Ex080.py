# Registrar valores e já cadastrar na ordem, sem usar o sorted
# Variáveis
lista = []

for c in range(0, 5):
    # Entrada do valor
    valor = int(input(f"Informe o {c+1}º valor: "))

    if c == 0 or valor > lista[-1]:  # Primeira execução apenas adiciona o valor ou se ele for maior que o último/maior
        lista.append(valor)
        print("Adicionado no final da lista")

    else:
        for i in range(0, len(lista)):  # Verifica cada valor da lista enquanto não for menor que um índice e não chegar
            if valor <= lista[i]:        # ao final da lista (última posição igual a comprimento menos 1)
                lista.insert(i, valor)
                print(f"Adicionado na posição {i} da lista")
                break

print(lista)
