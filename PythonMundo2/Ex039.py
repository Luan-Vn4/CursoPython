# Alistamento
import datetime
anoN = int(input("Informe o ano de nascimento: "))
ano = datetime.date.today().year
if ano - anoN < 18:
    print(f"Você ainda irá alistar-se!\nFaltam {18 - (ano-anoN)} anos")
elif ano - anoN == 18:
    print("Você está pronto para se alistar!")
else:
    print(f"Você passou do prazo de alistamento! Já passaram {(ano - anoN) - 18} anos")
