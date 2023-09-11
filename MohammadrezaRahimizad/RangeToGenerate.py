


def float_range(start, stop):
    while start < stop:
        yield start
        start += 0.01

def alphabet(start, stop, step):
    start = start.upper()
    stop = stop.upper()
    alphabetString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a = alphabetString.find(start)
    b = alphabetString.find(stop)

    for i in alphabetString[a:b:step]:
        yield i




if __name__ == "__main__":

    for i in float_range(2.3, 3.78):
        print("{:.2f}".format(i))

    for char in alphabet("c", "y", 1):
        print(char)





