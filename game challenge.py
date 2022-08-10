from random import *

userName = input("What is your name? ")
print(f"All right {userName}!! Welcome to this game. I've thought in a number between 1 to 100. You have 8 shoots to "
      f"guess it")
numberList = list(range(1, 101))
numberChoice = choice(numberList)
userAttempts = 8
userWin = 0

userList = ["1", "2", "3", "4", "5", "6", "7", "8"]
for number in userList:
    userChoice = input(f"Tell me a number: ")
    userChoice = int(userChoice)
    userAttempts -= 1
    userWin += 1
    if numberChoice == userChoice:
        print(f"You won!!. My number was {numberChoice} and yours was {userChoice}. You made it in {userWin} attempts!")
        break
    elif userChoice not in range(1, 100):
        print(f"Try again. Your number {userChoice} is out of the limit accepted. You have {userAttempts} "
              f"more attempts!")
    elif userAttempts == 0:
        print(f" You lost {userName}. You are out of attempts. My number was {numberChoice}")
        break

    elif userChoice > numberChoice:
        print(f" Your selected number is higher than mine. Keep trying. You have {userAttempts} more attempts!")
    elif userChoice < numberChoice:
        print(f" Your selected number is lower than mine. Keep trying. You have {userAttempts} more attempts!")


