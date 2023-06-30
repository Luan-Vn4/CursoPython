# Palavras identificar vogais
from unidecode import unidecode

vogais = []
# palavras = ("Coco", "Kiwi", "Maracujá", "Tapioca", "Suquita", "Melancia", "Purê")
palavras = ("Aprender", "Programar", "Linguagem", "Python", "Curso", "Grátis", "Estudar", "Praticar", "Trabalhar",
            "Mercado", "Programador", "Futuro")

for p in palavras:
    for c in range(0, len(p)):
        if unidecode(p[c].upper()) in 'AEIOU':
            vogais += p[c]
    print(f"{p} possui as vogais: {vogais}")
    vogais.clear()
