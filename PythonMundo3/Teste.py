import csv
with open(r'C:\Users\Notebook\Desktop\Texto1.csv', 'a') as arquivo:
    print('', end='')
    csv.writer(arquivo).writerow((5, 'Jujubo', 99, 'M'))
with open(r'C:\Users\Notebook\Desktop\Texto1.csv', 'r') as arquivo:
    an = list(csv.reader(arquivo, delimiter=','))
print(an)
