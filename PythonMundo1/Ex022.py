# Programa que leia o nome e mostre: (nome minúsculo), (nome maiúsculo), (quantas letras sem considerar o espaço)
# (letras no primeiro nome)
nome = input("Informe seu nome: ")
print(f"Minúsculo: {nome.lower()}")
print(f"Maiúsculo: {nome.upper()}")
print(f"Letras ao todo: {len(nome.replace(' ', ''))}")
lista = nome.split()
print(f"Letras do primeiro nome: {len(lista[0])}")