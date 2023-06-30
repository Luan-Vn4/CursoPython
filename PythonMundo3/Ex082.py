# Verificar se a expressão está correta
exp = list(input("Digite a expressão: "))
# and exp[::-1].index(')') < exp[::-1].index('(')
if exp.count('(') == exp.count(')'):
    while '(' in exp and ')' in exp:
        if exp.index('(') < exp.index(')'):
            exp.pop(exp.index('('))
            exp.pop(exp.index(')'))
        else:
            print("Expressão inválida")
            break
    else:
        print("Expressõa válida")
else:
    print("Expressão inválida")
