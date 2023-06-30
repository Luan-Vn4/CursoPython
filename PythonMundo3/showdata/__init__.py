def listar(arquivo, delimitador=',', cod='utf-8'):
    """
    :param arquivo: Endereço do arquivo .csv a ser lido (usar raw String, caso windows)
    :param delimitador: Tipo de sinal usado para delimitar as informações no arquivo csv. Padrão=','
    :param cod: Codificação do texto. Padrão='utf-8'
    :return: none
    """
    import csv

    # Abertura do arquivo
    with open(r'{}'.format(arquivo), mode='r', encoding=cod) as dados:
        lista = list(csv.reader(dados, delimiter=delimitador))  # Registros colocados dentro da lista

        # Verifica o tamanho de cada coluna
        # Verificada cada coluna, linha por linha (por isso invertido)
        tam_coluna = []
        for i2 in range(0, len(lista[0])):
            for i1 in range(0, len(lista)):
                if i1 == 0:
                    tam_coluna.append(len(lista[i1][i2]) + 8)
                else:
                    try:
                        if tam_coluna[i2] < len(lista[i1][i2]):
                            tam_coluna[i2] = len(lista[i1][i2]) + 8
                    except IndexError:
                        pass

        # Vizualização dos dados
        # Cada coluna de cada linha da linha será escrita em uma tabela
        for nl, linha in enumerate(lista):
            for nc, coluna in enumerate(linha):
                if nc == 0:
                    if nl == 0:  # Fundo branco no cabeçalho da tabela
                        print(f"\033[07m|{coluna.upper():^{tam_coluna[nc]}}|\033[m", end='')
                    else:
                        print(f"|{coluna:^{tam_coluna[nc]}}|", end='')
                elif nc == 1:
                    if nl == 0:  # Fundo branco no cabeçalho da tabela
                        print(f"\033[07m{coluna.upper():^{tam_coluna[nc]}}|\033[m", end='')
                    else:
                        print(f"{coluna:^{tam_coluna[nc]}}|", end='')
                else:
                    if nl == 0:  # Fundo branco no cabeçalho da tabela
                        print(f"\033[07m{coluna.upper():^{tam_coluna[nc]}}|\033[m", end='')
                    else:
                        print(f"{coluna:^{tam_coluna[nc]}}|", end='')

                if nc == (len(linha) - 1):
                    print()
                    print('-'*(sum(tam_coluna) + len(tam_coluna)+1))


def adicionar(arquivo, registro=()):
    """
    :param arquivo: Endereço do arquivo .csv onde adicionar registro ou criar
    :param registro: Iterator com o registro
    :return: none
    """
    import csv
    with open(arquivo, mode='a', newline='') as arquivo:
        csv.writer(arquivo).writerow(registro)

def lenght(arquivo):
    import csv
    with open(r"{}".format(arquivo), 'r') as dados:
        lista = list(csv.reader(dados))
        return len(lista)
