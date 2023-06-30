# Programa que lê o nome e duas notas de vários alunos. Depois, mostra o boletim com suas médias e mostra a nota
# Individual de cada aluno, caso pergunte
from time import sleep
idt = 0
alunos = []  # Alunos = [[nome, notas], [nome, notas]]

while True:
    # Entrada de dados
    alunos.append(['', []])  # Adiciona um novo aluno
    alunos[idt][0] = input(f"Informe o nome do {idt+1}º aluno: ")  # Informa o nome do aluno no identificador(idt) atual
    for c in range(0, 2):  # Adiciona as duas notas do aluno do 'idt' atual
        alunos[idt][1].append(float(input(f"Nota {c+1}: ")))

    # Verificar continuação
    while True:
        resposta = input("Adicionar mais um aluno? [S/N]")
        if resposta in "SsNn":
            break
    if resposta in 'Nn':
        break
    else:
        idt += 1

# Boletim
print("~"*34)
print(f"{'Id.':^5}|{'NOME':^20}|{'MÉDIA':^7}")
print("-"*34)
for idt in range(0, len(alunos)):
    print(f"{idt:^5}|{alunos[idt][0]:^20}|{(alunos[idt][1][0]+alunos[idt][1][1])/2:^7.1f}")

# Acesso às notas individuais
print("-"*40)
while idt != 999:
    idt = int(input("Ver notas do aluno(id): (999 interrompe)"))
    if idt != 999:
        try:
            print(f"Aluno: {alunos[idt][0]}\nNotas: {alunos[idt][1]}")
        except IndexError as e1:
            print("Identificador inválido! Tente novamente...")
        except ValueError as e1:
            print("Valor inválido! Apenas números...")
    print("-"*40)

# Encerramento
print("\033[031mEncerrando", end='')
for c in range(0, 3):
    sleep(0.5)
    print(".", end='')
