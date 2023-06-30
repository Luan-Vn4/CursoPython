# Criar uma matriz 3x3 com valores lidos pelo programa com formatação correta
matriz = [[], [], []]
c, somap, soma3 = 1, 0, 0
# Entrada de valores
for i1 in range(0, 3):
    for i2 in range(0, 3):
        matriz[i1].append(int(input(f"Informe o número da posição {c}: ")))
        if matriz[i1][i2] % 2 == 0:
            somap += matriz[i1][i2]
        if i2 == 2:
            soma3 += matriz[i1][i2]
        c += 1

# Mostra matriz
print(('+'+'-'*5)+('+'+'-'*6)*2+'+')
for n in matriz:
    print(f'{n[0]:^6}|{n[1]:^6}|{n[2]:^6}')
    print(('+'+'-'*5)+('+'+'-'*6)*2+'+')

print(f"A soma dos valores pares é: {somap}")
print(f"A soma dos valores da terceira coluna é: {soma3}")
print(f"O maior valor da segunda linha é: {max(matriz[1])}")
