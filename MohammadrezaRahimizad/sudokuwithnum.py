
import turtle
import random

turtle.hideturtle()
turtle.speed(0)


choices = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Table:
t1 = set()
t2 = set()
t3 = set()
t4 = set()
t5 = set()
t6 = set()
t7 = set()
t8 = set()
t9 = set()

# Rows:
r1 = set()
r2 = set()
r3 = set()
r4 = set()
r5 = set()
r6 = set()
r7 = set()
r8 = set()
r9 = set()

# Columons:
c1 = set()
c2 = set()
c3 = set()
c4 = set()
c5 = set()
c6 = set()
c7 = set()
c8 = set()
c9 = set()

turtle.penup()
turtle.goto(-90, -90)
turtle.pendown()
turtle.width(5)

# Row 1 :

number = random.choice(tuple(choices))
turtle.write(number, font = ("Arial", 11, "normal"))
t1.add(number)
r1.add(number)
c1.add(number)

turtle.fd(20)
number = random.choice(tuple(choices.difference(r1)))
turtle.write(number, font = ("Arial", 11, "normal"))
t1.add(number)
r1.add(number)
c2.add(number)


turtle.fd(20)
number = random.choice(tuple(choices.difference(r1)))
turtle.write(number, font = ("Arial", 11, "normal"))
t1.add(number)
r1.add(number)
c3.add(number)


turtle.fd(20)
number = random.choice(tuple(choices.difference(r1)))
turtle.write(number, font=("Arial", 11, "normal"))
t2.add(number)
r1.add(number)
c4.add(number)

turtle.fd(20)
number = random.choice(tuple(choices.difference(r1)))
turtle.write(number, font=("Arial", 11, "normal"))
t2.add(number)
r1.add(number)
c5.add(number)


turtle.fd(20)
number = random.choice(tuple(choices.difference(r1)))
turtle.write(number, font=("Arial", 11, "normal"))
t2.add(number)
r1.add(number)
c6.add(number)


turtle.fd(20)
number = random.choice(tuple(choices.difference(r1)))
turtle.write(number, font=("Arial", 11, "normal"))
t3.add(number)
r1.add(number)
c7.add(number)

turtle.fd(20)
number = random.choice(tuple(choices.difference(r1)))
turtle.write(number, font=("Arial", 11, "normal"))
t3.add(number)
r1.add(number)
c8.add(number)

turtle.fd(20)
number = random.choice(tuple(choices.difference(r1)))
turtle.write(number, font=("Arial", 11, "normal"))
t3.add(number)
r1.add(number)
c9.add(number)

# Row 2 :

turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.fd(20)
turtle.rt(90)
turtle.width(1)
turtle.fd(8)


number = random.choice(tuple(choices.difference(t1, c1)))
turtle.write(number, font=("Arial", 11, "normal"))
t1.add(number)
r2.add(number)
c1.add(number)

turtle.fd(20)
for _ in t3.difference(t1, r2, c2):
    number = random.choice(tuple(t3.difference(t1, r2, c2)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t1.add(number)
    r2.add(number)
    c2.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t1, r2, c3):
    number = random.choice(tuple(choices.difference(t1, r2, c3)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t1.add(number)
    r2.add(number)
    c3.add(number)
    break

turtle.fd(20)
for _ in t3.difference(t2, r2, c4):
    number = random.choice(tuple(t3.difference(t2, r2, c4)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t2.add(number)
    r2.add(number)
    c4.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t2, r2, c5):
    number = random.choice(tuple(choices.difference(t2, r2, c5)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t2.add(number)
    r2.add(number)
    c5.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t2, r2, c6):
    number = random.choice(tuple(choices.difference(t2, r2, c6)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t2.add(number)
    r2.add(number)
    c6.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t3, r2, c7):
    number = random.choice(tuple(choices.difference(t3, r2, c7)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t3.add(number)
    r2.add(number)
    c7.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t3, r2, c8):
    number = random.choice(tuple(choices.difference(t3, r2, c8)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t3.add(number)
    r2.add(number)
    c8.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t3, r2, c9):
    number = random.choice(tuple(choices.difference(t3, r2, c9)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t3.add(number)
    r2.add(number)
    c9.add(number)
    break

# Row 3 :

turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.width(5)
turtle.fd(20)
turtle.rt(90)
turtle.width(1)
turtle.fd(8)

for _ in choices.difference(t1, r3, c1):
    number = random.choice(tuple(choices.difference(t1, c1)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t1.add(number)
    r3.add(number)
    c1.add(number)
    break

turtle.fd(20)
for _ in t3.difference(t1, r3, c2):
    number = random.choice(tuple(t3.difference(t1, r3, c2)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t1.add(number)
    r3.add(number)
    c2.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t1, r3, c3):
    number = random.choice(tuple(choices.difference(t1, r3, c3)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t1.add(number)
    r3.add(number)
    c3.add(number)
    break

turtle.fd(20)
for _ in t3.difference(t2, r3, c4):
    number = random.choice(tuple(t3.difference(t2, r3, c4)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t2.add(number)
    r3.add(number)
    c4.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t2, r3, c5):
    number = random.choice(tuple(choices.difference(t2, r3, c5)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t2.add(number)
    r3.add(number)
    c5.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t2, r3, c6):
    number = random.choice(tuple(choices.difference(t2, r3, c6)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t2.add(number)
    r3.add(number)
    c6.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t3, r3, c7):
    number = random.choice(tuple(choices.difference(t3, r3, c7)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t3.add(number)
    r3.add(number)
    c7.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t3, r3, c8):
    number = random.choice(tuple(choices.difference(t3, r3, c8)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t3.add(number)
    r3.add(number)
    c8.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t3, r3, c9):
    number = random.choice(tuple(choices.difference(t3, r3, c9)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t3.add(number)
    r3.add(number)
    c9.add(number)
    break


# Row 4 :

turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.width(5)
turtle.fd(20)
turtle.rt(90)
turtle.width(3)
turtle.fd(8)

for _ in choices.difference(t4, r4, c1):
    number = random.choice(tuple(choices.difference(t4, c1)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t4.add(number)
    r4.add(number)
    c1.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t4, r4, c2):
    number = random.choice(tuple(t3.difference(t4, r4, c2)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t4.add(number)
    r4.add(number)
    c2.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t4, r4, c3):
    number = random.choice(tuple(choices.difference(t4, r4, c3)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t4.add(number)
    r4.add(number)
    c3.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t5, r4, c4):
    number = random.choice(tuple(t3.difference(t5, r4, c4)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t5.add(number)
    r4.add(number)
    c4.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t5, r4, c5):
    number = random.choice(tuple(choices.difference(t5, r4, c5)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t5.add(number)
    r4.add(number)
    c5.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t5, r4, c6):
    number = random.choice(tuple(choices.difference(t5, r4, c6)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t5.add(number)
    r4.add(number)
    c6.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t6, r4, c7):
    number = random.choice(tuple(choices.difference(t6, r4, c7)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t6.add(number)
    r4.add(number)
    c7.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t6, r4, c8):
    number = random.choice(tuple(choices.difference(t6, r4, c8)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t6.add(number)
    r4.add(number)
    c8.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t6, r4, c9):
    number = random.choice(tuple(choices.difference(t6, r4, c9)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t6.add(number)
    r4.add(number)
    c9.add(number)
    break

# Row 5 :


turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.width(5)
turtle.fd(20)
turtle.rt(90)
turtle.width(1)
turtle.fd(8)

for _ in choices.difference(t4, r5, c1):
    number = random.choice(tuple(choices.difference(t4, c1)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t4.add(number)
    r5.add(number)
    c1.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t4, r5, c2):
    number = random.choice(tuple(choices.difference(t4, r5, c2)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t4.add(number)
    r5.add(number)
    c2.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t4, r5, c3):
    number = random.choice(tuple(choices.difference(t4, r5, c3)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t4.add(number)
    r5.add(number)
    c3.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t5, r5, c4):
    number = random.choice(tuple(choices.difference(t5, r5, c4)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t5.add(number)
    r5.add(number)
    c4.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t5, r5, c5):
    number = random.choice(tuple(choices.difference(t5, r5, c5)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t5.add(number)
    r5.add(number)
    c5.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t5, r5, c6):
    number = random.choice(tuple(choices.difference(t5, r5, c6)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t5.add(number)
    r5.add(number)
    c6.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t6, r5, c7):
    number = random.choice(tuple(choices.difference(t6, r5, c7)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t6.add(number)
    r5.add(number)
    c7.add(number)
    break


turtle.fd(20)
for _ in choices.difference(t6, r5, c8):
    number = random.choice(tuple(choices.difference(t6, r5, c8)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t6.add(number)
    r5.add(number)
    c8.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t6, r5, c9):
    number = random.choice(tuple(choices.difference(t6, r5, c9)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t6.add(number)
    r5.add(number)
    c9.add(number)
    break

# Row 6

turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.width(5)
turtle.fd(20)
turtle.rt(90)
turtle.width(1)
turtle.fd(8)

for _ in choices.difference(t4, r6, c1):
    number = random.choice(tuple(choices.difference(t4, c1)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t4.add(number)
    r6.add(number)
    c1.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t4, r6, c2):
    number = random.choice(tuple(choices.difference(t4, r6, c2)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t4.add(number)
    r6.add(number)
    c2.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t4, r6, c3):
    number = random.choice(tuple(choices.difference(t4, r6, c3)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t4.add(number)
    r6.add(number)
    c3.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t5, r6, c4):
    number = random.choice(tuple(choices.difference(t5, r6, c4)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t5.add(number)
    r6.add(number)
    c4.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t5, r6, c5):
    number = random.choice(tuple(choices.difference(t5, r6, c5)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t5.add(number)
    r6.add(number)
    c5.add(number)
    break


turtle.fd(20)
for _ in choices.difference(t5, r6, c6):
    number = random.choice(tuple(choices.difference(t5, r6, c6)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t5.add(number)
    r6.add(number)
    c6.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t6, r6, c7):
    number = random.choice(tuple(choices.difference(t6, r6, c7)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t6.add(number)
    r6.add(number)
    c7.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t6, r6, c8):
    number = random.choice(tuple(choices.difference(t6, r6, c8)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t6.add(number)
    r6.add(number)
    c8.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t6, r6, c9):
    number = random.choice(tuple(choices.difference(t6, r6, c9)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t6.add(number)
    r6.add(number)
    c9.add(number)
    break

# Row 7 :

turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.width(5)
turtle.fd(20)
turtle.rt(90)
turtle.width(3)
turtle.fd(8)


for _ in choices.difference(t7, r7, c1):
    number = random.choice(tuple(choices.difference(t7, c1)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t7.add(number)
    r7.add(number)
    c1.add(number)
    break


turtle.fd(20)
for _ in choices.difference(t7, r7, c2):
    number = random.choice(tuple(choices.difference(t7, r7, c2)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t7.add(number)
    r7.add(number)
    c2.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t7, r7, c3):
    number = random.choice(tuple(choices.difference(t7, r7, c3)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t7.add(number)
    r7.add(number)
    c3.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t8, r7, c4):
    number = random.choice(tuple(choices.difference(t8, r7, c4)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t8.add(number)
    r7.add(number)
    c4.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t8, r7, c5):
    number = random.choice(tuple(choices.difference(t8, r7, c5)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t8.add(number)
    r7.add(number)
    c5.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t8, r7, c6):
    number = random.choice(tuple(choices.difference(t8, r7, c6)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t8.add(number)
    r7.add(number)
    c6.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t9, r7, c7):
    number = random.choice(tuple(choices.difference(t9, r7, c7)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t9.add(number)
    r7.add(number)
    c7.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t9, r7, c8):
    number = random.choice(tuple(choices.difference(t9, r7, c8)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t9.add(number)
    r7.add(number)
    c8.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t9, r7, c9):
    number = random.choice(tuple(choices.difference(t9, r7, c9)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t9.add(number)
    r7.add(number)
    c9.add(number)
    break

# Row 8 :

turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.width(5)
turtle.fd(20)
turtle.rt(90)
turtle.width(1)
turtle.fd(8)


for _ in choices.difference(t7, r8, c1):
    number = random.choice(tuple(choices.difference(t7, c1)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t7.add(number)
    r8.add(number)
    c1.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t7, r8, c2):
    number = random.choice(tuple(choices.difference(t7, r8, c2)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t7.add(number)
    r8.add(number)
    c2.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t7, r8, c3):
    number = random.choice(tuple(choices.difference(t7, r8, c3)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t7.add(number)
    r8.add(number)
    c3.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t8, r8, c4):
    number = random.choice(tuple(choices.difference(t8, r8, c4)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t8.add(number)
    r8.add(number)
    c4.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t8, r8, c5):
    number = random.choice(tuple(choices.difference(t8, r8, c5)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t8.add(number)
    r8.add(number)
    c5.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t8, r8, c6):
    number = random.choice(tuple(choices.difference(t8, r8, c6)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t8.add(number)
    r8.add(number)
    c6.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t9, r8, c7):
    number = random.choice(tuple(choices.difference(t9, r8, c7)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t9.add(number)
    r8.add(number)
    c7.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t9, r8, c8):
    number = random.choice(tuple(choices.difference(t9, r8, c8)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t9.add(number)
    r8.add(number)
    c8.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t9, r8, c9):
    number = random.choice(tuple(choices.difference(t9, r8, c9)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t9.add(number)
    r8.add(number)
    c9.add(number)
    break

# Row 9 :

turtle.fd(12)
turtle.bk(180)
turtle.lt(90)
turtle.width(5)
turtle.fd(20)
turtle.rt(90)
turtle.width(1)
turtle.fd(8)


for _ in choices.difference(t7, r9, c1):
    number = random.choice(tuple(choices.difference(t7, c1)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t7.add(number)
    r9.add(number)
    c1.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t7, r9, c2):
    number = random.choice(tuple(choices.difference(t7, r9, c2)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t7.add(number)
    r9.add(number)
    c2.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t7, r9, c3):
    number = random.choice(tuple(choices.difference(t7, r9, c3)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t7.add(number)
    r9.add(number)
    c3.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t8, r9, c4):
    number = random.choice(tuple(choices.difference(t8, r9, c4)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t8.add(number)
    r9.add(number)
    c4.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t8, r9, c5):
    number = random.choice(tuple(choices.difference(t8, r9, c5)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t8.add(number)
    r9.add(number)
    c5.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t8, r9, c6):
    number = random.choice(tuple(choices.difference(t8, r9, c6)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t8.add(number)
    r9.add(number)
    c6.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t9, r9, c7):
    number = random.choice(tuple(choices.difference(t9, r9, c7)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t9.add(number)
    r9.add(number)
    c7.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t9, r9, c8):
    number = random.choice(tuple(choices.difference(t9, r9, c8)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t9.add(number)
    r9.add(number)
    c8.add(number)
    break

turtle.fd(20)
for _ in choices.difference(t9, r9, c9):
    number = random.choice(tuple(choices.difference(t9, r9, c9)))
    turtle.write(number, font=("Arial", 11, "normal"))
    t9.add(number)
    r9.add(number)
    c9.add(number)
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
