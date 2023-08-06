# import random
from random import sample
import re

gameChices=['Rock' , 'Paper' ,'Scissors']

ValidChoice= {" R " : "Rock",
              " P " : "Paper",
              " S " :"Scissors",
              " Q " :"Qiute"}
WinList=["PR","RS","SP"]
LostList=["PS","RP","SR"]
yes_choices = ['yes', 'y']
no_choices = ['no', 'n']
gameSet= set(ValidChoice.keys())
gameSet =gameSet.union(ValidChoice.values())

UserWinCount =0
ComWinCount = 0
RunMessage = ("I had : {0} and your choice was : {1}")
userWinMessage = ("Oh, you are lucky \n")
QuiteMessage = ("Thnks you for playing  this game . I realy enjoyed it")
equalMessage = ("try again . Seems our Choice are the same. \n")
ComWinMessage = ("hahaaa , I'm Winner \n clap , clap ,happiness \n ")
WelcomeMessage = ("Welcome to My Game! \nWe Want to play the game of Rock - paper - Scissors \nHope you Enjoy it!")
selectMessage =("Please select either Rock , paper or Scissors (or QUIT to exit) : ")
print("****************************************************************")
print(WelcomeMessage)
print("****************************************************************")
checkCountGame = True
QuiteGame= False
while (QuiteGame == False):
          ComWinCount=0
          UserWinCount=0
          checkCountGame = True
          while(checkCountGame):
              countGame= input('please enter the number of games  :')
              countGame =countGame.strip()

              if (countGame.isnumeric()) != 0:
                  countGame =int(countGame)
                  checkCountGame = False
              else:
                 print("input Is Not Valid . please Type in an 'integer'\n")

          while(countGame > 0):
              MyChoice = ""
              while(len(MyChoice) == 0):
                     print("*" * 60)
                     MySelect = input('\nPlease select either Rock , paper or Scissors (or QUIT to exit) : ')
                     MySelect = " "+MySelect + " "
                     for value  in gameSet:
                         if re.search(value, MySelect, re.IGNORECASE):
                            MyChoice = value
                            break

                     if (len(MyChoice) == 0):
                         print("'"+ MySelect +"'"+ " is not a valid choice , please try again ")
                     else:                 break

              if MyChoice == "Q":
                  print("Thanks you play this game")
                  QuiteGame = True
                  break



               # Prints list of random items of given length
              ComChoice =sample(gameChices, 1)
              Choiceitems=(MyChoice.strip().upper())[0] + (ComChoice[0])[0]
              #1print(Choiceitems)

              if  Choiceitems  in WinList:
                   UserWinCount += 1
                   print(userWinMessage)
                   countGame -= 1
              else :
                  if Choiceitems in LostList:
                       ComWinCount += 1
                       print(ComWinMessage)
                       countGame -= 1
                  else:
                    print(equalMessage)

              print(RunMessage.format(ComChoice[0], MyChoice))
              print("\n Computer Score is : "  + str(ComWinCount))
              print(" Your Score is : " + str(UserWinCount))

          print("*" * 40)
          if(ComWinCount > UserWinCount):
              print("\n WooHooo . I HAVE WON THE Game\n")
          else:
              if(ComWinCount < UserWinCount):
                  print("\n CONGRATULATIONS .REALY GOD JOB . YOU WON \n")
              else:
                  print("\n WE ARE EQUAL . WE BOTH WON \n")


          print("*" * 40)
          playAgain = 0
          while (playAgain == 0):
               user_input = input('\n Care to play another game ? Yes/No  :  ')
               if user_input.lower() in yes_choices:
                    playAgain = 1
               elif user_input.lower() in no_choices:
                    QuiteGame = True
                    playAgain  = 1
               else:
                    print('Type yes or no')
