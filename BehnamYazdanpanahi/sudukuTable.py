import turtle

screen = turtle.Screen()
screen.setup(700, 700)

table = turtle.Turtle()
table.speed(0)
table.hideturtle()

# draw lines for rows
for row in range(10):
    if row % 3 == 0:
        table.pensize(3)
    else:
        table.pensize(1)

    table.penup()
    table.goto(-220, 220 - row * 50)
    table.pendown()
    table.forward(450)

table.right(90)

# draw lines for columns
for col in range(10):
    if col % 3 == 0:
        table.pensize(3)
    else:
        table.pensize(1)

    table.penup()
    table.goto(-220 + col * 50, 220)
    table.pendown()
    table.forward(450)

screen.exitonclick()


