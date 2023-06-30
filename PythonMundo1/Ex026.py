# Ler uma frase e mostrar: (Quantas vezes aparece "a"), (Em que posição ela aparece pela primeira vez),
# (Em que posição ela aparece pela última vez
frase = input("Digite uma frase: ").strip()
qA = frase.upper().count("A")
qAP = frase.upper().find("A")
qAF = frase.upper().rfind("A")
print(f'A frase possui "{qA}" letras A\n'
      f'A primeira letra A aparece na posição {qAP+1}\n'
      f'A última letra A aparece na posição {qAF+1}')
