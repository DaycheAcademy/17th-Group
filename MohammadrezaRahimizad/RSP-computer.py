

import random



print('*' * 40)
print('Welcom to my game\n'
      'Hope you enjoy your experience!')
print('*' * 40)
print("Let's Go For Gaming.\n")

#---------------------------------------------------------

validChoices = (('r', 'rock'), ('s', 'scissor'), ('p', 'paper'))
print(type(validChoices))

playerWinMessage = (("You nailed it."),
                    ("You won."),
                    ("You had the right choice."),
                    ("Oh no I lost.")
                    )

computerWinMessage = (("I had the right choice"),
                      ("I Won"),
                      ("I naild it"),
                      ("Yes! Chance is with me.")
                      )

while True:

    inp = input("Please Just Type 'Start' or 'S'\nTo Start The Game: " )
    if inp.lower() == 'start' or inp.lower() == 's':
        print("game started")

        while True:
            winScore = 0
            playerWinscore = 0
            computerWinscore = 0
            inp = input("Please enter a value of winning score:(Number) ""\n")


            if not inp.isdigit():
                print("I Need A Number")
                continue

            if inp.isdigit():
                winScore += int(inp)
                print("\n\t\t\t\t","* " * 8,
                      "\n\t\t\t\t  Game Started!", "\n\t\t\t\t ", "* " * 7)
                print("\nYou choose win score to: ", winScore)


                while True:
                    while True:
                        inp = input("\nPlease select\n"
                                    "Rock, Paper or Scissors"
                                    "(Or QUIT For Exit): ")


                        if inp.lower() == 'rock' or inp.lower() == 'r':
                            computerChoise = random.choice(validChoices)[1]

                            if computerChoise == 'scissor' or computerWinscore == 's':
                                playerWinscore += 1
                                print("I chose: ", computerChoise,
                                      "\nYou chose: ", inp,
                                      "\n", random.choice(playerWinMessage),
                                      "\nYour Score is: ", playerWinscore,
                                      "\nMy Score Is: ", computerWinscore)

                            if computerChoise == 'paper' or computerWinscore == 'p':
                                computerWinscore += 1
                                print("I chose: ", computerChoise,
                                      "\nYou chose: ", inp,
                                      "\n", random.choice(computerWinMessage),
                                      "\nYour Score is: ", playerWinscore,
                                      "\nMy Score Is: ", computerWinscore)

                            if computerChoise == 'rock' or computerWinscore == 'r':
                                print("I chose: ", computerChoise,
                                      "\nYou chose: ", inp,
                                      "\nWe had the same choice!",
                                      "\nYour Score is: ", playerWinscore,
                                      "\nMy Score Is: ", computerWinscore)

                        if inp.lower() == 'paper' or inp.lower() == 'p':
                            computerChoise = random.choice(validChoices)[1]

                            if computerChoise == 'rock' or computerWinscore == 'r':
                                playerWinscore += 1
                                print("I chose: ", computerChoise,
                                      "\nYou chose: ", inp,
                                      "\n", random.choice(playerWinMessage),
                                      "\nYour Score is: ", playerWinscore,
                                      "\nMy Score Is: ", computerWinscore)

                            if computerChoise == 'scissor' or computerWinscore == 's':
                                computerWinscore += 1
                                print("I chose: ", computerChoise,
                                      "\nYou chose: ", inp,
                                      "\n", random.choice(computerWinMessage),
                                      "\nYour Score is: ", playerWinscore,
                                      "\nMy Score Is: ", computerWinscore)

                            if computerChoise == 'paper' or computerWinscore == 'p':
                                print("I chose: ", computerChoise,
                                      "\nYou chose: ", inp,
                                      "\nWe had the same choice!",
                                      "\nYour Score is: ", playerWinscore,
                                      "\nMy Score Is: ", computerWinscore)

                        if inp.lower() == 'scissor' or inp.lower() == 's':
                            computerChoise = random.choice(validChoices)[1]

                            if computerChoise == 'paper' or computerWinscore == 'p':
                                playerWinscore += 1
                                print("I chose: ", computerChoise,
                                      "\nYou chose: ", inp,
                                      "\n", random.choice(playerWinMessage),
                                      "\nYour Score is: ", playerWinscore,
                                      "\nMy Score Is: ", computerWinscore)

                            if computerChoise == 'rock' or computerWinscore == 'r':
                                computerWinscore += 1
                                print("I chose: ", computerChoise,
                                      "\nYou chose: ", inp,
                                      "\n", random.choice(computerWinMessage),
                                      "\nYour Score is: ", playerWinscore,
                                      "\nMy Score Is: ", computerWinscore)

                            if computerChoise == 'scissor' or computerWinscore == 's':
                                print("I chose: ", computerChoise,
                                      "\nYou chose: ", inp,
                                      "\nWe had the same choice!",
                                      "\nYour Score is: ", playerWinscore,
                                      "\nMy Score Is: ", computerWinscore)

                        if playerWinscore == winScore:
                            print("\n\t\t\tOh no! I lost\n"
                                  "\t\t\tCongratulation To You\n")
                            break
                        if computerWinscore == winScore:
                            print("\n\t\t\tYes! Chance is with me.\n"
                                  "\t\t\t\tI Won The Game\n")
                            break

                        if inp.lower() == 'quit' or inp.lower() == 'q':
                            print("* " * 10,
                                  '\n You Quit the game\n',
                                  "* " * 9)
                            break
                    break





                inp = input("If you want to play again TYPE(Y)\n"
                            "Otherwise TYPE anything : ")
                if inp.lower() == "y":
                    continue

            break