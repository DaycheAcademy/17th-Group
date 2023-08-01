# 3 = wiz
# 5 = hop
# 3 and 5 = hopwiz


#for number in range(1,21):
    #print('hop') if number % 5 == 0 else print(number)

for num in range(1,100):
    game = 'hopwiz' if not num % 15 else\
            'wiz' if not num % 3 else\
            'hop' if not num % 5 else\
            str(num)
    print(game)