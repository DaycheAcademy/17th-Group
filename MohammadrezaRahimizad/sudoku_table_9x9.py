


import time
import turtle

turtle.hideturtle()
turtle.speed(0)


for _ in range(4):
    turtle.color("red")
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(180)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(180)
    turtle.right(90)

turtle.forward(20)
turtle.right(90)

for _ in range(4):
    turtle.color("red")
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(180)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(180)
    turtle.right(90)

turtle.forward(20)
turtle.right(90)

for _ in range(4):
    turtle.color("black")
    turtle.width(5)
    turtle.forward(180)
    turtle.right(90)

for _ in range(4):
    turtle.color("black")
    turtle.width(3)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(180)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)



#time.sleep(2) # wait's for 2 seconds
turtle.done()

