# Sortear 4 alunos em ordem aleatória
import random
alunos = []
print (alunos)
for c in range(4):
    alunos.append(input(f"Informe o nome do {c+1}º aluno: "))
print(f"A ordem dos alunos é: {random.sample(alunos, k=2)}")
