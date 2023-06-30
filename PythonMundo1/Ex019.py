# Ler nome de quatro alunos e sortear um deles
import random
alunos = []
for c in range(4):
    alunos.append(input(f"Informe o nome do {c+1}º aluno: "))
print(f"O aluno escolhido para apagar o quadro foi: {random.choice(alunos)}")
