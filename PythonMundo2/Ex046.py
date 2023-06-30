# 10 até 0 com pausa de 1 seg
import time
for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print('BOOOOM!')