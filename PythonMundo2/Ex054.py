# Quem é maior de idade e quem não é
import datetime
nomes = []
nascimento = []
maioridade = []
menoridade = []
anoA = datetime.date.today().year
somaM = 0
somam = 0
# Entrada dos nomes e idade
for i in range(7):
    nomes.append(input(f"Insira o {i+1}º nome: "))
    nascimento.append(int(input(f"Insira o ano de nascimento: ")))
# Contagem
for i in range(7):
    if anoA - nascimento[i] >= 18:
        maioridade.append(nomes[i])
        somaM = somaM + 1
    else:
        menoridade.append(nomes[i])
        somam = somam + 1
# Resultados
print(f"{somaM} pessoas atingiram a maioridade. São eles: {maioridade}")
print(f"{somam} pessoas estão na menoridade. São eles: {menoridade}")
