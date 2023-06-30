# Ler 5 valores e mostrar maior, menor e posição deles na lista
# Variáveis
maior = menor = 0
maxPos, minPos = [], []
lista = []

# Entrada e comparação de valores
for c in range(0, 5):
    lista.append(int(input(f"Informe o {c+1}º número: ")))
    # Primeira ocorrência apenas atribui o valor
    if c == 0:
        maior = menor = lista[c]
        maxPos.append(c)
        minPos.append(c)
    else:
        #  Verificação Maior
        if lista[c] > maior:
            maior = lista[c]
            maxPos.clear()  # Valor maior limpa a lista de posições e adiciona a posição do maior atual
            maxPos.append(c)
        elif lista[c] == maior:
            maxPos.append(c)  # Caso seja igual ao maior atual, apenas adiciona a posição dele

        #  Verificação menor
        if lista[c] < menor:
            menor = lista[c]
            minPos.clear()  # Valor menor limpa a lista de posições e adiciona a posição do menor atual
            minPos.append(c)
        elif lista[c] == menor:
            minPos.append(c)  # Caso seja igual ao menor atual, apenas adiciona a posição dele

# Resultados
print(f"{lista}")
print(f"O maior valor é {maior} | Posições: {maxPos}")
print(f"O menor valor é {menor} | Posições: {minPos}")
