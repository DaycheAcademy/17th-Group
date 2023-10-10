def factor(x):
    a = 1
    answer = 0
    while (a + 1) <= x:
        answer = a * (a + 1)
        a += 1
    return answer


if __name__ == '__main__':
    print('factoryel:', factor(4))

