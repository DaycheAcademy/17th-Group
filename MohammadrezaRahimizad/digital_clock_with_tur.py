

import time
import turtle

turtle.hideturtle()
turtle.speed(0)

turtle.color("white")
turtle.bk(100)

turtle.color("gray")
while True:
    turtle.clear()
    turtle.write(time.strftime("%Y-%m-%d %H:%M:%S"), font = ("Arial", 16, "normal"))
    time.sleep(1)





