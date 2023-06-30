# Média do aluno
n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
media = (n1 + n2)/2

if media < 5:
    print(f"\033[31mREPROVADO!\033[m\nNota: {media}")
elif media < 7:
    print(f"Recuperação!\nNota: {media}")
else:
    print(f"\033[32mParabéns, você foi aprovado!\033[m\nNota: {media}")
