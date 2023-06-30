# Ler o nome, idade e sexo de 4 pessoas e mostrar:
# Média de idade, nome do homem mais velho e quantas mulheres têm menos de 20
nome = []
idade = []
sex = []
# Entrada
for i in range(4):
    nome.append(input(f"Informe o {i + 1}º nome: "))
    idade.append(int(input(f"Informe a idade: ")))
    sex.append(input("Sexo: (M) (F)"))
# Média da idade
soma = 0
for i in range(4):
    soma = soma + idade[i]
media = soma / 4
# Nome do homem mais velho
vM = 0
hV = ''
for i in range(4):
    if sex[i] == 'M':
        if idade[i] > vM:
            vM = idade[i]
            hV = nome[i]
# Quantas mulheres tem menos de 20 anos
m20 = []
for i in range(4):
    if sex[i] == 'F':
        if idade[i] < 20:
            m20.append(nome[i])
# Resultados
print(f"Média das idades: {media}")
print(f"Homem mais velho: {hV}")
print(f"{len(m20)} mulheres acima de 20: {m20}")
