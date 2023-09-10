
import turtle
import random

turtle.hideturtle()
turtle.speed(0)

# Table:
t1 = []
t2 = []
t3 = []
t4 = []
t5 = []
t6 = []
t7 = []
t8 = []
t9 = []

# Columons:
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []
c8 = []
c9 = []

turtle.color("white")
turtle.bk(90)
turtle.width(5)
turtle.rt(90)
turtle.fd(90)
turtle.lt(90)
turtle.color("black")

# Row 1 :
choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number = random.choice(choices)
turtle.write(number, font = ("Arial", 11, "normal"))
choices.remove(number)
t1.append(number)
c1.append(number)

turtle.fd(20)
number = random.choice(choices)
turtle.write(number, font = ("Arial", 11, "normal"))
choices.remove(number)
t1.append(number)
c2.append(number)


turtle.fd(20)
number = random.choice(choices)
turtle.write(number, font = ("Arial", 11, "normal"))
choices.remove(number)
t1.append(number)
c3.append(number)


turtle.fd(20)
number = random.choice(choices)
turtle.write(number, font=("Arial", 11, "normal"))
choices.remove(number)
t2.append(number)
c4.append(number)

turtle.fd(20)
number = random.choice(choices)
turtle.write(number, font=("Arial", 11, "normal"))
choices.remove(number)
t2.append(number)
c5.append(number)


turtle.fd(20)
number = random.choice(choices)
turtle.write(number, font=("Arial", 11, "normal"))
choices.remove(number)
t2.append(number)
c6.append(number)


turtle.fd(20)
number = random.choice(choices)
turtle.write(number, font=("Arial", 11, "normal"))
choices.remove(number)
t3.append(number)
c7.append(number)


turtle.fd(20)
number = random.choice(choices)
turtle.write(number, font=("Arial", 11, "normal"))
choices.remove(number)
t3.append(number)
c8.append(number)

turtle.fd(20)
number = random.choice(choices)
turtle.write(number, font=("Arial", 11, "normal"))
choices.remove(number)
t3.append(number)
c9.append(number)

# Row 2 :
choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.fd(20)
turtle.rt(90)
turtle.width(1)
turtle.fd(8)


for i in range(100):
    number = random.choice(t3)
    if not number in t1 :
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t1.append(number)
        c1.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(t3)
    if not number in t1 :
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t1.append(number)
        c2.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(t3)
    if not number in t1 :
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t1.append(number)
        c3.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t2 :
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t2.append(number)
        c4.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t2 :
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t2.append(number)
        c5.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t2 :
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t2.append(number)
        c6.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t3:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t3.append(number)
        c7.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t3 :
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t3.append(number)
        c8.append(number)
        break

turtle.fd(20)
number = random.choice(choices)
turtle.write(number, font=("Arial", 11, "normal"))
choices.remove(number)
t3.append(number)
c9.append(number)

# Row 3 :
choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.width(5)
turtle.fd(20)
turtle.rt(90)
turtle.width(1)
turtle.fd(8)

for i in range(100):
    number = random.choice(choices)
    if not number in t1 :
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t1.append(number)
        c1.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t1 :
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t1.append(number)
        c2.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t1 :
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t1.append(number)
        c3.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t2 :
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t2.append(number)
        c4.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t2 :
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t2.append(number)
        c5.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t2 :
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t2.append(number)
        c6.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t3 :
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t3.append(number)
        c7.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t3 :
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t3.append(number)
        c8.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t3 :
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t3.append(number)
        c9.append(number)
        break


# Row 4 :
choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.width(5)
turtle.fd(20)
turtle.rt(90)
turtle.width(3)
turtle.fd(8)

for i in range(100):
    number = random.choice(t2)
    if not number in t4 and not number in c1:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t4.append(number)
        c1.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t4 and not number in c2:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t4.append(number)
        c2.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t4 and not number in c3:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t4.append(number)
        c3.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t5 and not number in c4:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t5.append(number)
        c4.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t5 and not number in c5:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t5.append(number)
        c5.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t5 and not number in c6:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t5.append(number)
        c6.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t6 and not number in c7:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t6.append(number)
        c7.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t6 and not number in c8:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t6.append(number)
        c8.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t6 and not number in c9:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t6.append(number)
        c9.append(number)
        break

# Row 5 :
choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.width(5)
turtle.fd(20)
turtle.rt(90)
turtle.width(1)
turtle.fd(8)

for i in range(100):
    number = random.choice(t6)
    if not number in t4 and not number in c1:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t4.append(number)
        c1.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t4 and not number in c2:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t4.append(number)
        c2.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t4 and not number in c3:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t4.append(number)
        c3.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t5 and not number in c4:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t5.append(number)
        c4.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t5 and not number in c5:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t5.append(number)
        c5.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t5 and not number in c6:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t5.append(number)
        c6.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t6 and not number in c7:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t6.append(number)
        c7.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t6 and not number in c8:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t6.append(number)
        c8.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t6 and not number in c9:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t6.append(number)
        c9.append(number)
        break

# Row 6
choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.width(5)
turtle.fd(20)
turtle.rt(90)
turtle.width(1)
turtle.fd(8)

for i in range(100):
    number = random.choice(t6)
    if not number in t4 and not number in c1:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t4.append(number)
        c1.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t4 and not number in c2:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t4.append(number)
        c2.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t4 and not number in c3:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t4.append(number)
        c3.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t5 and not number in c4:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t5.append(number)
        c4.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t5 and not number in c5:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t5.append(number)
        c5.append(number)
        break


turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t5 and not number in c6:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t5.append(number)
        c6.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t6 and not number in c7:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t6.append(number)
        c7.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t6 and not number in c8:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t6.append(number)
        c8.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t6 and not number in c9:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t6.append(number)
        c9.append(number)
        break

# Row 7 :
choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.width(5)
turtle.fd(20)
turtle.rt(90)
turtle.width(3)
turtle.fd(8)


for i in range(100):
    number = random.choice(choices)
    if not number in t7 and not number in c1:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t7.append(number)
        c1.append(number)
        break


turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t7 and not number in c2:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t7.append(number)
        c2.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t7 and not number in c3:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t7.append(number)
        c3.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t8 and not number in c4:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t8.append(number)
        c4.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t8 and not number in c5:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t8.append(number)
        c5.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t8 and not number in c6:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t8.append(number)
        c6.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t9 and not number in c7:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t9.append(number)
        c7.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t9 and not number in c8:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t9.append(number)
        c8.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t9 and not number in c9:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t9.append(number)
        c9.append(number)
        break

# Row 8 :
choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.width(5)
turtle.fd(20)
turtle.rt(90)
turtle.width(1)
turtle.fd(8)


for i in range(100):
    number = random.choice(choices)
    if not number in t7 and not number in c1:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t7.append(number)
        c1.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t7 and not number in c2:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t7.append(number)
        c2.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t7 and not number in c3:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t7.append(number)
        c3.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t8 and not number in c4:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t8.append(number)
        c4.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t8 and not number in c5:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t8.append(number)
        c5.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t8 and not number in c6:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t8.append(number)
        c6.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t9 and not number in c7:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t9.append(number)
        c7.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t9 and not number in c8:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t9.append(number)
        c8.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t9 and not number in c9:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t9.append(number)
        c9.append(number)
        break

# Row 9 :
choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.width(5)
turtle.fd(20)
turtle.rt(90)
turtle.width(1)
turtle.fd(8)


for i in range(100):
    number = random.choice(choices)
    if not number in t7 and not number in c1:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t7.append(number)
        c1.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t7 and not number in c2:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t7.append(number)
        c2.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t7 and not number in c3:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t7.append(number)
        c3.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t8 and not number in c4:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t8.append(number)
        c4.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t8 and not number in c5:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t8.append(number)
        c5.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t8 and not number in c6:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t8.append(number)
        c6.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t9 and not number in c7:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t9.append(number)
        c7.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t9 and not number in c8:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t9.append(number)
        c8.append(number)
        break

turtle.fd(20)
for i in range(100):
    number = random.choice(choices)
    if not number in t9 and not number in c9:
        turtle.write(number, font=("Arial", 11, "normal"))
        choices.remove(number)
        t9.append(number)
        c9.append(number)
        break

# Completing main table
turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.width(5)
turtle.fd(20)
turtle.rt(90)
turtle.fd(180)
turtle.rt(90)
turtle.fd(180)
turtle.width(3)

# Completing inner tables
turtle.rt(90)
turtle.fd(60)
turtle.rt(90)
turtle.fd(180)
turtle.lt(90)
turtle.fd(60)
turtle.lt(90)
turtle.fd(180)


# Completing lines
turtle.rt(90)
turtle.bk(120)
turtle.lt(90)
turtle.width(1)

for _ in range(4):
    turtle.rt(90)
    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(180)
    turtle.lt(90)
    turtle.fd(20)
    turtle.lt(90)
    turtle.fd(180)

turtle.done()
