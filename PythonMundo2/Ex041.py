# Classificação natação (9 anos: Mirim) (14: infantil) (19: junior) (20: Senio) (Acima: Master)
import datetime
bran, norm = '\033[7m', '\033[m'
print(f"{bran}Até 9 anos: Mirim{norm}\n{bran}Até 14 anos: Infantil{norm}"
      f"\n{bran}Até 19 anos: Junior{norm}\n{bran}Até 20 anos: Sênior{norm}\n{bran}Acima: Master{norm}")
anoN = int(input("Informe o ano de nascimento: "))
idade = datetime.date.today().year - anoN

if idade < 9:
    print(f"Idade: {idade}\nClassificação: Mirim")
elif idade < 14:
    print(f"Idade: {idade}\nClassificação: Infantil")
elif idade < 19:
    print(f"Idade: {idade}\nClassificação: Junior")
elif idade < 20:
    print(f"Idade: {idade}\nClassificação: Sênior")
else:
    print(f"Idade: {idade}\nClassificação: Master")
