while True:
    try:
        qt, ano = input().split()
        qt, ano = int(qt), int(ano)
        users = set()
        qt_repetidos = 0
        for i in range(qt):
            user = ''
            for nome in input().split():
                user = f'{user}{nome[0]}'
            if user in users:
                qt_repetidos+=1
            else:
                users.add(user)
                
        print(qt_repetidos)
    except:
        break