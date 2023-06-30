from math import sin, cos, tan, radians
# Seno, cosseno e tangente do ângulo
ang = float(input("Informe um ângulo: "))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print(f"Ângulo: {ang}º\nSeno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}")
