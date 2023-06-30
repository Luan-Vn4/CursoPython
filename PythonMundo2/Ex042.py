# Pode formar um triângulo ou não? e o tipo
from math import sqrt
lado = []
m = 0
# Entrada e verificação do maior lado
for i in range(3):
    lado.append(float(input(f"Informe o lado {i + 1}º lado: ")))
    if lado[i] > m:
        m = lado[i]

# Resposta
if lado[0] < lado[1]+lado[2] and lado[1] < lado[0] + lado[2] and lado[2] < lado[1] + lado[0]: # Verifica se forma
    print(f"Os lados {lado[0]}, {lado[1]}, {lado[2]} podem formar um triângulo", end=" ")
    # Verificar o tipo
    if lado[0] == lado[1] and lado[1] == lado[2]:
        print("equilátero")
    elif lado[0] == lado[1] or lado[0] == lado[2] or lado[1] == lado[2]:
        if lado[0] == sqrt(lado[1]**2 + lado[2]**2) or lado[1] == sqrt(lado[0]**2 + lado[2]**2)\
                or lado[2] == sqrt(lado[1]**2 + lado[0]**2):
            print("retângulo", end= " ")
        print("isósceles")
    else:
        if lado[0] == sqrt(lado[1]**2 + lado[2]**2) or lado[1] == sqrt(lado[0]**2 + lado[2]**2)\
                or lado[2] == sqrt(lado[1]**2 + lado[0]**2):
            print("retângulo", end=" ")
        print("escaleno")

        
else:
    print(f"Os lados {lado[0]}, {lado[1]}, {lado[2]} NÃO podem formar um triângulo")
