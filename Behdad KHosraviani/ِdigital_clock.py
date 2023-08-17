import turtle as t
import time

# step 1: getting clock

time_now = time.localtime(time.time())
time_now_digit = '{}:{}:{}'.format(time_now.tm_hour,
                                    time_now.tm_min,
                                    time_now.tm_sec)

print(time_now_digit)

# step 2 : show the time

t.hideturtle()

t.write(time_now_digit, align='center',
        font=('Arial', 80, 'normal'))

t.done()
