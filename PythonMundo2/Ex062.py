# n primeiros termos da sequência de Fibonacci
pos = int(input("Até qual posição deseja ver a sequência de Fibonacci?\n"))
a, b = 0, 1
c = 1
seq = ''
while c <= pos:
    if c < pos:
        seq += str(b) + " -> "
    else:
        seq += str(b)
    """anterior = a
    posterior = b
    a = posterior
    b += anterior"""
    a, b = b, a + b
    c += 1
print(f'{seq}')
