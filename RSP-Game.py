








print('*' * 40)
print('Welcom to my game\n'
      'Hope you enjoy your experience!')
print('*' * 40)
print("Let's Go For Gaming.\n")

#---------------------------------------------------------

while True:
    inp = input("Please Type 'Start' or 'S' To Start The Game: ")
    if inp.lower() == 'start' or inp.lower() == 's':

        winScore = 0
        player1WinScore = 0
        player2WinScore = 0

        inp = input('please enter value of winning score:(Number) ')
        if not inp.isdigit():
            print("I Need A Number!!")
            continue
        else:
            winScore += int(inp)
            print('you choose win score to:', winScore)

            while True:

                player1 = input("\nPlayer1 Please select\n"
                                "Rock, Paper or Scissors(Or QUIT For Exit): ")
                if player1.lower() == 'quit' or player1.lower() == 'q':
                    print('\nPlayer2 Quit the game\n')
                    break

                player2 = input("\nPlayer2 Please select\n"
                                "Rock, Paper or Scissors(Or QUIT For Exit): ")
                if player2.lower() == 'quit' or player2.lower() == 'q':
                    print('\nPlayer2 Quit the game\n')
                    break

                if player1.lower() == 'rock' or player1.lower() == 'r':
                    if player2.lower() == 'scissors' or player2.lower() == 's':
                        player1WinScore += 1
                        print(f'player1 choose: {player1}\n'
                              f'player2 choose: {player2}\n'
                              f'Nice job player1, You won!\n'
                              'Player1 Score is: ', player1WinScore,
                              '\nPlayer2 Score Is: ',player2WinScore)
                    if player2.lower() == 'paper' or player2.lower() == 'p':
                        player2WinScore += 1
                        print(f'player1 choose: {player1}\n'
                              f'player2 choose: {player2}\n'
                              f'Nice job player2, You won!\n'
                              'Player1 Score is: ', player1WinScore,
                              '\nPlayer2 Score Is: ',player2WinScore)


                if player1.lower() == 'paper' or player1.lower() == 'p':
                    if player2.lower() == 'rock' or player2.lower() == 'r':
                        player1WinScore += 1
                        print(f'player1 choose: {player1}\n'
                              f'player2 choose: {player2}\n'
                              f'Nice job player1, You won!\n'
                              'Player1 Score is: ', player1WinScore,
                              '\nPlayer2 Score Is: ',player2WinScore)
                    if player2.lower() == 'scissors' or player2.lower() == 's':
                        player2WinScore += 1
                        print(f'player1 choose: {player1}\n'
                              f'player2 choose: {player2}\n'
                              f'Nice job player2, You won!\n'
                              'Player1 Score is: ', player1WinScore,
                              '\nPlayer2 Score Is: ',player2WinScore)


                if player1.lower() == 'scissors' or player1.lower() == 's':
                    if player2.lower() == 'paper' or player2.lower() == 'p':
                        player1WinScore += 1
                        print(f'player1 choose: {player1}\n'
                              f'player2 choose: {player2}\n'
                              f'Nice job player1, You won!\n'
                              'Player1 Score is: ', player1WinScore,
                              '\nPlayer2 Score Is: ',player2WinScore)
                    if player2.lower() == 'rock' or player2.lower() == 'r':
                        player2WinScore += 1
                        print(f'player1 choose: {player1}\n'
                              f'player2 choose: {player2}\n'
                              f'Nice job player2, You won!\n'
                              'Player1 Score is: ', player1WinScore,
                              '\nPlayer2 Score Is: ',player2WinScore)


                if player1WinScore == winScore:
                    print('\nPlayer1\nYou nailed it!\nYou won the game!!')
                    break
                if player2WinScore == winScore:
                    print('\nPlayer2\nYou nailed it!\nYou won the game!!\n')
                    break
    else:
        print("\n       Please just type 'S' or 'Start'\n")






