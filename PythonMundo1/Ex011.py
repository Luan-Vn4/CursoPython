# Área da parede e tinta
import math

largura = float(input("Qual a largura da parede? "))
altura = float(input("Qual a altura da parede? "))
a = altura * largura
qT = a/2
print(f"A parede tem {a:.2f}m² e precisa de {qT:.2f} litros de tinta (l/2m²)")
