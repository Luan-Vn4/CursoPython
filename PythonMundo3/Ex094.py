# Ler nome, sexo e idade de várias pessoas, guardar em uma lista de dicionários e mostrar:
# (quantidade de pessoas cadastradas), (média de idade do grupo), (lista com todas as mulheres) e (lista de pessoas
# com idade acima da média)
c = 1
dados, pessoa = [], {}

while True:
    # Entrada de dados (nome, sexo e idade)
    pessoa['nome'] = input(f"Nome {c}: ")  # Entrada do NOME

    while True:  # Entrada do SEXO
        try:
            pessoa['sexo'] = input("Sexo(M/F): ")
            if pessoa['sexo'] not in 'MmFf' or pessoa['sexo'] == '':
                raise ValueError("Entrada Inválida!")
            else:
                if pessoa['sexo'] in 'Mm':
                    pessoa['sexo'] = 'Masculino'
                else:
                    pessoa['sexo'] = 'Feminino'
                break
        except ValueError as e1:
            print(e1)

    while True:  # Entrada da idade
        try:
            pessoa['idade'] = int(input("Idade: "))
            break
        except ValueError as e1:
            print('Entrada inválida!')

    # Cadastra o usuário
    dados.append(pessoa.copy())

    # Pergunta se deseja continuar
    proc = ' '
    while proc not in 'SsNn':
        proc = input("Deseja continuar? [S/N]")
    if proc in 'Nn':
        break
    else:
        c += 1
        pessoa.clear()

# Mostra os dados recolhidos em tabela
print(f"{'-=-'*10}")
print(f"{'BANCO DE DADOS':^30}")
print(f"{'-=-'*10}")
print(f"{'Nome':<20}|{'Sexo':^12}|{'Idade':^8}")
print('-'*43)
for i in dados:
    nome = i['nome']
    sexo = i['sexo']
    idade = i['idade']
    print(f"{nome:<20}|{sexo:^12}|{idade:^7}")
print('-'*43)

# Verificando informações
somaM = 0  # Soma para calcular média
mulheres = []  # Lista com mulheres do grupo

for i in dados:
    somaM += i['idade']
    if i['sexo'] == 'Feminino':
        mulheres.append(i)
media = somaM/len(dados)

acim_media = []
for i in dados:
    if i['idade'] > media:
        acim_media.append(i)

# Mostrando informações
print(f"a) {len(dados)} pessoas foram cadastradas")
print(f"b) Média de idade do grupo: {media}")
print(f"c) {len(mulheres)} mulheres no grupo: ", end='')
for c in range(0, len(mulheres)):
    if c < (len(mulheres) - 1):
        print(mulheres[c]['nome'] + ', ', end='')
    else:
        print(mulheres[c]['nome'])
print(f"d) Pessoas com idade acima da média:")
for i in acim_media:
    print(f"Nome = {i['nome']} | Sexo: {i['sexo']} | Idade: {i['idade']}")
