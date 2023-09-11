import turtle as t

t.hideturtle()
t.speed(0)
# creating 9*9 Sudoku Table

t.forward(252)
t.right(90)
t.forward(5 * 56)
t.right(90)

# 1*1 line 56 and 3*3 lines
t.pensize(1)
for i in range(25):
    if i < 19:
        if i == 9:
            t.right(90)
        elif i < 9:
            if i % 2 == 0:
                t.forward(504)
                t.right(90)
                t.forward(56)
                t.right(90)
            else:
                t.forward(504)
                t.left(90)
                t.forward(56)
                t.left(90)
        else:
            if i % 2 != 0:
                t.forward(504)
                t.right(90)
                t.forward(56)
                t.right(90)
            else:
                t.forward(504)
                t.left(90)
                t.forward(56)
                t.left(90)
    else:
        t.pensize(3)
        if i > 22:
            t.right(180)
        if i < 22:
            if i % 2 == 0:
                t.forward(504)
                t.right(90)
                t.forward(3 * 56)
                t.right(90)
            else:
                t.forward(504)
                t.left(90)
                t.forward(3 * 56)
                t.left(90)
        else:
            if i % 2 != 0:
                t.forward(3 * 56)
                t.right(90)
                t.forward(504)
                t.right(90)
            else:
                t.forward(3 * 56)
                t.left(90)
                t.forward(504)
                t.left(90)

# ----------------------------------------------------------------
# creating outer line

t.pensize(5)
for i in range(4):
    t.forward(504)
    t.left(90)


t.done()
