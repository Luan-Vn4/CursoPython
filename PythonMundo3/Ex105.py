# Função que lê várias notas e retorna um dicionário, mostra situação opcional
# Também mostra: maior nota, menor nota, média e quantidade de notas
def turma(*notas, sit=False):
    media = sum(notas)/len(notas)
    # Definindo situação
    if media >= 7:
        situ = 'Boa'
    elif media > 6:
        situ = 'Razoável'
    else:
        situ = 'Tristeza'

    # Verificando retorno
    if sit is True:
        return {'Quantidade': len(notas), 'Maior': max(notas), 'Menor': min(notas),
                'Media': media, 'sit': situ}
    else:
        return {'Quantidade': len(notas), 'Maior': max(notas), 'Menor': min(notas),
                'Media': media}

resp = turma(3.5, 10, 6.5, 2, 1, 4, sit=True)
print(resp)
