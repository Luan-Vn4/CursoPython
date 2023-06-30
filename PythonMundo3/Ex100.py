# função para sortear 5 números e colocar numa lista e depois outra função de somar os pares dessa lista
def sortear():
    from random import randint
    num = [randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60)]
    return num


def soma_par(num):
    soma = 0
    for i in num:
        if i % 2 == 0:
            soma += i
    return soma


numeros = sortear()
print(f"Valores sorteados: {numeros} ")
print(f"Soma dos valores pares: {soma_par(numeros)}")
