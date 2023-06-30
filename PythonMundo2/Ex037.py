# Binário Octal e Hexadecimal
num = int(input("Digite um número inteiro: "))
resp = int(input("Conversão:\n[1]Binário\n[2]Octal\n[3]Hexadecimal\nOpção: "))
match resp:
    case 1:
        print(f"{num} convertido para binário é: {bin(num)[2:]}")
    case 2:
        print(f"{num} convertido para octal é: {oct(num)[2:]}")
    case 3:
        print(f"{num} convertido para hexadecimal é: {hex(num)[2:]}")
    case _:
        print("Opção Inválida!")
