# Pode formar um triângulo ou não?
lado = []
for i in range(3):
    lado.append(float(input(f"Informe o lado {i + 1}º lado: ")))
if lado[0] < lado[1]+lado[2] and lado[1] < lado[0] + lado[2] and lado[2] < lado[1] + lado[0]:
    print(f"Os lados {lado[0]}, {lado[1]}, {lado[2]} podem formar um triângulo")
else:
    print(f"Os lados {lado[0]}, {lado[1]}, {lado[2]} NÃO podem formar um triângulo")
