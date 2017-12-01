import random

print("We are going to play spoof!")
userExcited = input("Are you excited? (Y/N) ")
if userExcited == "Y":
    print("YAAAAAY!")
else:
    print("Well that's boring")

rounds = int(input("How many rounds would you like to play? "))

userScore = 0
computerScore = 0

for i in range(0, rounds):
    computerCoins = random.randint(0, 3)
    userCoins = int(input("How many coins would you like? (0-3)"))
    computerGuess = random.randint(computerCoins, (6 + (computerCoins - 3)) + 1)
    if userCoins > 3:
        print("Incorrect input... You lose")
        continue
    guessing = True
    firstTime = True
    while guessing:
        if not firstTime:
            if computerGuess == (userCoins + computerCoins):
                print("Computer got it")
                computerScore += 1
            else:
                print("Computer got it wrong... But did you?")
        if firstTime:
            userGuess = int(input("How many coins do you think there are in total?"))
            firstTime = False
        elif userGuess < userCoins or userGuess > (6 + (userCoins - 3)):
            userGuess = int(input("THAT ISN'T POSSIBLE, SKRUB! Guess again kiddo (0-3) "))
        else:
            if userGuess == (userCoins + computerCoins):
                print("YOU WIN!")
                userScore += 1
            else:
                print("Incorrect.... Next round please")
            guessing = False

print("You scored " + str(userScore) + " and the computer scored " +str(computerScore))
    
