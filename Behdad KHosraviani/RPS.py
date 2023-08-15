# we are a polite developer, lets greet the player

welcome_text = ''' WELCOME to RPS game,
 you may know the game by the way,
 when your decision is made just type:
 Rock , Paper or scissor
 now challenge me! :))'''

print(welcome_text)
print('********************************************')

# defining the core functions of the game

computer_score = 0
palyer_score = 0

def who_wins(computer_choice, human_choice):
    if computer_choice == human_choice:
        print('that was a draw , no point for either of us')
    elif computer_choice == "ss":
        if human_choice == "rk":
            print('human wins')
        else:
            print('computer')
    elif computer_choice == "rk":
        if human_choice == "pp":
            print('human wins')
        else:
            print('computer')
    else:
        if human_choice == "ss":
            print('human wins')
        else:
            print('computer')


# now we have the core function, lets take input from human
quite_list = ['q', "quit", "Q", 'Quit']


while True:
    time_play = input('how much rounds yoy may play? :(type quit to end) ').strip()
    if time_play.isdigit():
        time_play = int(time_play)
        break
    elif time_play in quite_list:
        break
    else:
        print('please enter a number.(type quit to end) ')

print(time_play)

# I would prefer to determine the computer choice just now

from random import choice

RPS = ['Rock','Paper','Scissor']
computer_choice = choice(RPS)
print(computer_choice)

# now we get to the hard part, taking input from the hurman

human_choice_list = ['Rock', 'Paper', 'Scissor', 'r', 'R', 'p', 'P', 's', 'S', 'ss', 'rock', 'paper', 'scissor']

if time_play not in quite_list :
    breaker = False
    while breaker == False:
        human_choice = input('Now try your chance! which one?(type quit to end)').split(sep=' ')
        human_choice.append("fix bug")
        for i in human_choice:
            if i in quite_list:
                print('game is done')
                q = True
                break
            if breaker == True:
                break
            for j in human_choice_list:
                if j == i:
                    human_choice = i
                    breaker = True
                    break
        else:
            print('Come on! don\'t play with me! enter a valid choice!')



