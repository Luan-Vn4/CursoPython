nome = 'Luan'
inv = '\033[7m'
nor = '\033[m'
print(f'Olá, prazer, {inv}{nome}{nor}')
print('Olá, prazer, {}{}{}'.format('\033[7m', nome, '\033[m'))
