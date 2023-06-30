# Ler números e só parar quando o usuário digitar 999 (soma não conta 999)
num = 0
soma = 0
while num != 999:
    num = int(input("Digite o número que deseja somar (999 encerra): "))
    if num != 999:
        soma += num

print(f"Programa encerrado!! {num}\n Soma dos números: {soma}")
