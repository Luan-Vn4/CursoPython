# Programa que cadastra pessoas com nome e idade em um arquivo de texto simples
# Cadastra e lista
import showdata as dados
res = 0
arquivo = r'C:\Users\Notebook\Desktop\Texto1.csv'

while res != 3:
    print('\033[34m', end='')
    print("-=-"*15)
    print(f"{'MENU':^45}")
    print("-=-"*15)
    print('\033[m', end='')
    print("1 - Ver pessoas cadastradas")
    print("2 - Cadastrar nova pessoas")
    print("3 - Sair do sistema")
    print("-=-"*15)
    while True:
        try:
            res = int(input("Opção: "))
            if str(res) not in '123':
                raise ValueError
            break
        except ValueError:
            print("Resposta inválida! Tente novamente...")
    print("~~~"*15)

    match res:
        case 1:
            dados.listar(arquivo, delimitador=',')
        case 2:
            idt = dados.lenght(arquivo)

            nome = input("Nome: ")  # Registro do nome
            while True:  # Registro da idade
                try:
                    idade = int(input("Idade: "))
                    break
                except ValueError:
                    print("Valor Inválido!")
            while True:  # Registro do sexo
                try:
                    sexo = input("Sexo: [M/F] ").upper()
                    if sexo[0].upper() not in 'FM' or sexo[0] == '':
                        raise ValueError
                    break
                except ValueError:
                    print("Sexo inválido!")

            registro = (idt, nome, idade, sexo)  # Cria registro com os dados
            dados.adicionar(arquivo, registro)  # Adiciona o registro ao arquivo
