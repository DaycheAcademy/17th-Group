

for i in range(2, 1001):
    for num in range(2, i):
        if not (i % num):
            break
    else:
        print(i)

print('=' * 40)


print("test for if it's a prime or not: ")
a = 9973 # change any number you want

for i in range(1, 1000000):
    if not (a % i):
        print(i)




