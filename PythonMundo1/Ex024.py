# Cidade começa com o nome "Santo"
nome = input("Informe o nome de uma cidade: ").strip()
subnomes = nome.split()
resposta = subnomes[0].upper().count("SANTO")
if resposta == 1:
    print('Essa cidade começa com "Santo"')
else:
    print(f'A cidade {nome} não começa com "Santo"')
