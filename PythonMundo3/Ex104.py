# Função leiaInt que funciona como um input, mas apenas aceita valores inteiros
def leia_int(args):
    while True:
        print(args, end=' ')
        try:
            __value__ = int(input())
            break
        except ValueError:
            print("\033[031mERRO! Digite um número inteiro.\033[m")
        except KeyboardInterrupt:
            print("\n\033[031mERRO! O usuário não digitou esse número...\033[m")
            __value__ = 0
            break
    return __value__

num = leia_int("Digite um número =):")
num2 = leia_int("Digite o segundo número =):")
print(f"Você digitou {num} e {num2}")
