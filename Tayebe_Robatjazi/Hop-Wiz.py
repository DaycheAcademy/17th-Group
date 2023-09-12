for i in range(100):
    if not i % 15:
        print('Hop-Wiz')
    elif not i % 5:
        print('Wiz')
    elif not i % 3:
        print('Hop')
    else:
        print(i)
