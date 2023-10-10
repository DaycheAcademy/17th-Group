import random
import turtle
import sudoku_table as st


# first we need a function to  generate random numbers from 1 to 10

def random_filler():
    num = random.randint(1, 9)
    turtle.write(num,
                 move=False, align='center',
                 font=('Arial', 15, 'normal'))


# now we create a function to fill the cells with random numbers

def fill_with_number():
    if st.validation_for_running == 1:
        turtle.up()
        turtle.setpos(252 - 28, -280 + 20)
        xpos = turtle.position()[0]
        ypos = turtle.position()[1]
        for j in range(9):
            for i in range(9):
                turtle.setpos(xpos - (i * 56), ypos + (j * 56))
                random_filler()
    else:
        print('first draw the table')


if __name__ == '__main__':

    st.drow_soduko_table()
    print(turtle.position())

    fill_with_number()

    turtle.done()
