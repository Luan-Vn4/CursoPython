import csv
with open(r'C:\Users\Notebook\Desktop\Texto1.csv', mode='r', encoding='utf-8') as dados:
    lista = list(csv.reader(dados, delimiter=','))
    print(lista[0])

    tamColuna = []
    for i2 in range(0, len(lista[0])):
        for i1 in range(0, len(lista)):
            if i1 == 0:
                tamColuna.append(len(str(lista[i1][i2])) + 8)
            else:
                if tamColuna[i2] < len(lista[i1][i2]):
                    tamColuna[i2] = len(lista[i1][i2]) + 8
    print(tamColuna)
    for nl, linha in enumerate(lista):
        for nc, coluna in enumerate(linha):
            if nc == 0:
                if nl == 0:
                    print(f"\033[07m|{coluna.upper():^{tamColuna[nc]}}|\033[m", end='')
                else:
                    print(f"|{coluna:^{tamColuna[nc]}}|", end='')
            elif nc == 1:
                if nl == 0:
                    print(f"\033[07m{coluna.upper():^{tamColuna[nc]}}|\033[m", end='')
                else:
                    print(f"{coluna:^{tamColuna[nc]}}|", end='')
            else:
                if nl == 0:
                    print(f"\033[07m{coluna.upper():^{tamColuna[nc]}}|\033[m", end='')
                else:
                    print(f"{coluna:^{tamColuna[nc]}}|", end='')

            if nc == (len(linha)-1):
                print()
                print('-'*(sum(tamColuna) + len(tamColuna)+1) )
