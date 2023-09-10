from random import choice

# we are a polite developer, lets greet the player

welcome_text = ''' WELCOME to RPS game,
 you may know the game by the way,
 when your decision is made just type:
 Rock , Paper or scissor
 now challenge me! :))'''

print(welcome_text)
print('********************************************')


# now we have the core function, lets take input from human
quite_list = ['q', "quit", "Q", 'Quit']

def round_play():
    while True:
        time_play = input('how much rounds yoy may play? :(type quit to end) ').strip()
        if time_play.isdigit():
            print('****************************')
            print('HaHa So you want to play pro!')
            print('Ok Darling :)))))))) ')
            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            return int(time_play)
        elif time_play in quite_list:
            return 'q'
        else:
            print('please enter a number.(type quit to end) ')


# now we get to the hard part, taking input from the human

human_choice_list = ['Rock', 'rock', 'r', 'R', 'Paper', 'paper', 'p', 'P', 'Scissor', 'scissor', 'sc', 'S', 's']
def take_input():
    while True:
        human_choice = input('Now try your chance! which one?(type quit to end)  ').split(sep=' ')
        human_choice.append("fix the bug")
        for i in human_choice:
            if i in quite_list:
                print('ok we can play later.good bye')
                return 'q'
            for j in human_choice_list:
                if i == j:
                    human_choice = i     # here we take the naive input
                    if human_choice in human_choice_list[0:4]:
                        return human_choice_list[0]
                    elif human_choice in human_choice_list[4:8]:
                        return human_choice_list[4]
                    else:
                        return human_choice_list[8]     # and here we make it clean
        else:
            print('Come on! don\'t play with me! Enter a valid choice!')
            print('================================================================')


# defining the core functions of the game

def game():

    computer_score = 0
    player_score = 0

    while computer_score + player_score != time_play :
        RPS = ['Rock', 'Paper', 'Scissor']
        computer_choice = choice(RPS)
        human_choice = take_input()
        if human_choice in quite_list:
            break
        elif computer_choice == human_choice:
            print('that was a draw , no point for either of us')
        elif computer_choice == "Scissor":
            if human_choice == "Rock":
                print('Ok you win')
                player_score += 1
                print('''*************************
                            *****************************''')
                print('I picked {} and you picked {}'.format(computer_choice, human_choice))
                print('your score is: ', player_score)
                print('................................')
                print('My score is: ', computer_score)
            else:
                print('I win !!!!!!!!')
                computer_score += 1
                print('''*************************
                                        *****************************''')
                print('I picked {} and you picked {}'.format(computer_choice, human_choice))
                print('your score is: ', player_score)
                print('................................')
                print('My score is: ', computer_score)

        elif computer_choice == "Rock":
            if human_choice == "Paper":
                print('you got lucky, you win!')
                player_score += 1
                print('''*************************
                                        *****************************''')
                print('I picked {} and you picked {}'.format(computer_choice, human_choice))
                print('your score is: ', player_score)
                print('................................')
                print('My score is: ', computer_score)
            else:
                print('It happens, sometime you loose in life')
                computer_score += 1
                print('''*************************
                                        *****************************''')
                print('I picked {} and you picked {}'.format(computer_choice, human_choice))
                print('your score is: ', player_score)
                print('................................')
                print('My score is: ', computer_score)
        else:
            if human_choice == "Scissor":
                print('be proud, you win!')
                player_score += 1
                print('''*************************
                                        *****************************''')
                print('I picked {} and you picked {}'.format(computer_choice, human_choice))
                print('your score is: ', player_score)
                print('................................')
                print('My score is: ', computer_score)
            else:
                print('Yes I win!')
                computer_score += 1
                print('''*************************
                                        *****************************''')
                print('I picked {} and you picked {}'.format(computer_choice, human_choice))
                print('your score is: ', player_score)
                print('................................')
                print('My score is: ', computer_score)
        print('================================================================')



# we run the game from here:
player_will = 'yes'

while player_will == 'yes':
    time_play = round_play()
    if time_play == 'q':
        print('OK we play later! good luck')
        break
    else:
        game()
        continue_will = input('Do you want to play again??[yes/no]').strip()
        yes_list = ['y', 'Y', 'Yes', 'yes']
        no_list = ['n', 'N', 'No', 'no']
        if continue_will in no_list or continue_will in quite_list:
            print('that was a good game! come back and play')
            player_will = 'No'
        elif continue_will in yes_list:
            player_will = 'Yes'
        else:
            print('you really enjoy to make fun of me:) ,say yes darling!')





