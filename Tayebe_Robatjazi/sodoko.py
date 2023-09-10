import turtle as t
t.hideturtle()
t.speed(200)
i= -1
count = 0
for _ in range(16):
    count += 1
    print(t.width(1))
    if (i == -1):
        print(t.left(90))
    else:
        print(t.right(90))
    print(t.forward(30))
    if (i == -1):
        print(t.left(90))
    else:
        print(t.right(90))
    if (count % 3 == 0 and count != 9):
        print(t.width(3))
    else:
        print(t.width(1))
    print(t.forward(270))
    if (count == 9): count += 1
    i *= -1
    if (count == 8 or count == 17):
        print(t.left(90))
        print(t.forward(30))

print(t.width(5))
for _ in range(4):
    print(t.left(90))
    print(t.forward(270))
t.done()