for num in range(1,1001):
    for num2 in range(2,num):
        if num % num2 == 0:
            break
    else:
        print(num)
