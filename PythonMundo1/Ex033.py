num = []
m = 0
for i in range(3):
    num.append(int(input(f"Informe o número da posição {i + 1}: ")))
me = num[0]
for i in range(3):
    if num[i] > m:
        m = num[i]
    if num[i] < me:
        me = num[i]
print(f"O maior número é: {m}")
print(f"O menor número é: {me}")
