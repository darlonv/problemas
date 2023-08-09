import re

while True:
    try:
        st = input().lower()
        if re.match(r'^(c.*|.*c)-(o.*|.*o)-(b.*|.*b)-(o.*|.*o)-(l.*|.*l)$',st):
            print('GRACE HOPPER')
        else:
            print('BUG')
    except:
        break