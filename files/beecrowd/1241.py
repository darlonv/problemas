import re

n = int(input())
for i in range(n):
    a,b = input().split()
    if re.match(f'[0-9]*{b}$', a):
        print('encaixa')
    else:
        print('nao encaixa')

