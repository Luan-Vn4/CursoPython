# Ler valores monetários
def input_coin(args=''):
    from time import sleep

    while True:
        try:
            print(args, end='')
            __value__ = float(input().replace(',', '.'))
            break
        except ValueError:
            print("\033[031mValor inválido! Tente novamente...\033[m")
            sleep(1)

    return __value__
