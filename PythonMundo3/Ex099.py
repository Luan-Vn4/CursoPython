# Função que retorna o maior valor
def maior(num):
    maiorn = 0
    c = 0
    for i in num:
        c += 1
        if i > maiorn:
            maiorn = i
    print(f'Números: {num}\nMaior número: {maiorn}\nQuantidade: {c}')


maior([5, 6, 7, 8])
maior([10, 9, 10])
