# Programa help
from time import sleep


def tittle(args):
    tam = len(args)
    print('-=-'*round((tam/3)))
    print(f'{args.upper():^{tam}}')
    print('-=-'*round((tam/3)))


def fundo(args=''):
    args = args.upper()
    if args == 'BRANCO':
        print('\033[07m', end='')
    elif args == 'VERDE':
        print('\033[42m', end='')
    elif args == 'AZUL':
        print('\033[44m', end='')
    elif args == 'VERMELHO':
        print('\033[41m', end='')
    else:
        print('\033[m', end='')


resp = ' '
while resp.upper() not in 'FIM':
    # Entrada
    fundo('Verde')
    tittle('Sistema de Ajuda PyHelp')
    fundo()

    resp = input("Função ou Biblioteca > ")
    if resp.upper() not in 'FIM':
        sleep(1)
        fundo('Azul')
        tittle(f"Acessando manual de: '{resp}'")
        fundo()
        sleep(1)
        fundo('Branco')
        help(resp)
        fundo()

fundo('Vermelho')
tittle("Encerrando...")
fundo()
print("Programa finalizado")
