# Programa que lê o nome, ano de nascimento e carteira de trabalho (registrar idade também)
# Caso carteira de trabalho != 0, registra ano de contratação e salário (registrar idade de aposentadoria)
from datetime import datetime
resp = ' '
current_year = datetime.today().year
pessoas = {}

# Coleta de dados
pessoas['nome'] = input("Nome: ")
pessoas['anoNasc'] = int(input("Ano de nascimento: "))
pessoas['idade'] = current_year - pessoas['anoNasc']

if pessoas['idade'] >= 18:  # Caso maior de idade, pergunta se trabalha
    while resp not in 'SsNn':
        resp = input("Você trabalha?\n")
    if resp in 'Ss':
        pessoas['cartTrab'] = input("Carteira de trabalho: ")
        pessoas['anoContrat'] = int(input("Ano de contratação: "))
        pessoas['anoAposent'] = pessoas['anoContrat'] + 35

        if pessoas['anoAposent'] > current_year:
            pessoas['idadeAposent'] = (pessoas['anoAposent'] - current_year) + pessoas['idade']
        else:
            pessoas['idadeAposent'] = pessoas['idade'] - (current_year - pessoas['anoAposent'])

print(f"Nome: {pessoas['nome']}")
print(f"Ano de nascimento | Idade: {pessoas['anoNasc']} | {pessoas['idade']}")
if 'cartTrab' in pessoas.keys():
    print(f"Carteira de trablaho: {pessoas['cartTrab']}")
    print(f"Ano de contratação: {pessoas['anoContrat']}")
    print(f"Ano de aposentadoria | Idade de aposentadoria: {pessoas['anoAposent']} | {pessoas['idadeAposent']}")
