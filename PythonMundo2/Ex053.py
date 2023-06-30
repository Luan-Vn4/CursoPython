# Verificar se é palíndromo
import unidecode
frase = input("Digite uma frase ou palavra: ").strip()
fraseP = unidecode.unidecode(frase.upper().replace(" ", ""))
print(fraseP)
fraseI = ''
for c in range(len(fraseP) - 1, -1, -1):
    fraseI = fraseI + fraseP[c]
print(fraseI)
if fraseI == fraseP:
    print(f"A palavra ou frase '{frase}' é um palíndromo")
else:
    print(f"A palvra ou frase '{frase}' não é um palíndromo")
