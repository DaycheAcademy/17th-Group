
import turtle as tur
import time

tur.hideturtle()
tur.speed(100)

while  True:
    tur.clear()
    value = time.localtime()

    currenthour ="%02d" % (value.tm_hour,)
    currentmin= "%02d" % (value.tm_min,)
    currentsec= "%02d" % (value.tm_sec,)

    tur.color("blue")
    tur.write(currenthour + ":"+ currentmin + ":", align="center" ,font=('Arial',60,'bold' ))
    tur.color("red")
    tur.write("{0:>16}".format(currentsec), align="center", font=('Arial', 60, 'bold'  ))
    time.sleep(1)

tur.done()

