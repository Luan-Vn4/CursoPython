# Tabuada de vários números
from time import sleep
while True:
    print("-=-" * 12)
    num = int(input("Deseja ver a tabuada de qual número?\n" + "-=-" * 12 + '\n'))
    if num > 0:
        print("~~~" * 12)
        for c in range(1, 11):
            sleep(0.21)
            print(f"{num} x {c} = {num*c}")
        print("~~~" * 12)
    else:
        print("~~~" * 12)
        print("Encerrando programa", end='')
        for c in range (0, 3):
            sleep(0.3)
            print(".", end='')
        break
