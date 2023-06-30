# Recebe texto e mostra ele enquadrado por linha com tamanho adaptável a ele
def escreva(txt):
    tam = len(txt) + 2
    print("~" * tam)
    print(f'{txt.upper():^{tam}}')
    print("~" * tam)


texto = input("Digite algo: ")
escreva(texto)
print("Alalala")
