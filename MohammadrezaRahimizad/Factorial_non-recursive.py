

def factorial(n):
    num = 1

    for i in range(n + 1):
        num *= i
        if i <= 1:
            num = 1
        print("The factorial of", i, "is", num)



if __name__ == "__main__":
    factorial(10)