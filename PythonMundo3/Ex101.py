# Função que lê a idade e diz se o voto é negado, opcional ou obrigatório
def voto(year):
    from datetime import datetime
    age = datetime.today().year - year
    if age < 16:
        return f'{age} | Negado'
    elif 16 <= age < 18 or age >= 70:
        return f'{age} | Opcional'
    else:
        return f'{age} | Obrigatório'


ano_nascimento = int(input("Digite o ano de nascimento: "))
print(f"Status de votação: {voto(ano_nascimento)}")
