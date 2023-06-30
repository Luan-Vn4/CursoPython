# Mostre o primeiro e último nome
nome = input("Informe um nome completo: ")
lista = nome.split()
print(f"Primeiro nome: {lista[0]}\nSegundo nome: {lista[len(lista) - 1]}")
