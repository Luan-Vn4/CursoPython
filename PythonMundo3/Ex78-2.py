# Ler 5 valores e mostrar maior, menor e posição deles na lista
# Variáveis
maior = menor = 0
maxPos, minPos = [], []
lista = []

# Entrada e comparação de valores
for c in range(0, 5):
    lista.append(int(input(f"Informe o {c+1}º número: ")))

# Comparação e listagem de posições
for p in range(0, len(lista)):
    if lista[p] == max(lista):
        maxPos.append(p)
    if lista[p] == min(lista):
        minPos.append(p)

# Resultados
print(f"{lista}")
print(f"O maior valor é {max(lista)} | Posições: {maxPos}")
print(f"O menor valor é {min(lista)} | Posições: {minPos}")
