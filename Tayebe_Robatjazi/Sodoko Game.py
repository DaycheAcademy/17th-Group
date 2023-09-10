import turtle as t
import random as r


t.hideturtle()
t.speed(100)
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


# Rows:
r1 = []
grid =[
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

def checkGrid(grid):
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                return False
    return True

choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 1
for _ in range(1,10):
    number = r.choice(choices)
    choices.remove(number)
    if not number in r1:
        r1.append(number)


ci = 1
cj = 1
count= 0
numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(9):
        for j in range(9):
             if (i == ci and j == cj ):
                    grid[i][j] = r1[count]
                    count += 1
                    cj += 3
                    if(count == 3 or count == 6):
                        cj = 1
                        ci += 3

def fillGrid(grid):

  for i in range(0, 81):
      row = i // 9
      col = i % 9

      if(grid[row][col] == 0):
           for value in numberList:
              if not (value in grid[row]):
                  if not value in (grid[0][col], grid[1][col], grid[2][col],
                                   grid[3][col], grid[4][col], grid[5][col],
                                   grid[6][col], grid[7][col], grid[8][col]):
                      if not value in (grid[((row // 3 )* 3)][((col // 3 )* 3)], grid[((row // 3 )* 3)][((col // 3 )* 3) +1], grid[((row // 3 )* 3)][((col // 3 )* 3) +2],
                                       grid[((row // 3 )* 3) +1][((col // 3 )* 3)], grid[((row // 3 )* 3) +1][((col // 3 )* 3) +1], grid[((row // 3 )* 3) +1][((col // 3 )* 3) +2],
                                       grid[((row // 3 )* 3) +2][((col // 3 )* 3)], grid[((row // 3 )* 3) +2][((col // 3 )* 3) +1], grid[((row // 3 )* 3) +2][((col // 3 )* 3) +2]):

                          grid[row][col] = value
                          if checkGrid(grid):
                              return True
                          else:
                              if fillGrid(grid):
                                  return True
           break
  grid[row][col] = 0

fillGrid(grid)
# for listmethod in grid:
#   print( listmethod)

for row in range(0, 9):
    for _ in range(0,2):
     number = r.choice(numberList)
     print((row, number-1))
     grid[row][number-1] = ' '

# for listmethod in grid:
#     print(listmethod)
#

withCol = -20
HightCol =3
count=0
for row in range(0, 9):
    for col in range(0, 9):
     t.up()
     t.setpos(withCol,HightCol)
     t.down()
     t.write(grid[row][col],font=(5))
     withCol += -30
     count +=1
     if(count % 9 == 0):
         HightCol += 30
         withCol = -20


t.done()