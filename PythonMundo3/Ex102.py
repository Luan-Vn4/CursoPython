# Função que calcula fatorial e tem opção de mostrar o processo, se desejado
def fatorial(n=0, show=False):
    """
    :param n: número a ser calculado
    :param show: define se irá mostrar o processo de cálculo (retorna String, caso True)
    :return: if show = True returns String, else returns Integer
    """
    proc = ''
    f = 1
    # Processo
    for c in range(1, n+1):
        if c < n:
            proc += str(c) + 'x'
        else:
            proc += str(c)
        f *= c

    # Verificação do retorno
    if show is False:
        return f
    else:
        return f'{n}! = {proc} = {f}'


print(fatorial(10, show=True))
help(fatorial)