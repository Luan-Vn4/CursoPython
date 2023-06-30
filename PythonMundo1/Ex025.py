# Verificar se tem "Silva" no nome
nome = input("Informe o nome completo: ")
dividido = nome.split()
if ('SILVA ' in nome.upper()) == False:
    print(f'O nome {nome} não contém "Silva"')
else:
    print(f'O nome {nome} contém "Silva"', end= '')
    for i in range(len(dividido)):
        if dividido[i].upper() == 'SILVA':
            print(f" na posição {i + 1}")
