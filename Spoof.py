import random
    
def use_learning(guesses):
    print(guesses)

try:
    print("We are going to play spoof!")
    userExcited = input("Are you excited? (Y/N) ")
    if userExcited == "Y":
        print("YAAAAAY!")
    else:
        print("Well that's boring")

    rounds = int(input("How many rounds would you like to play? "))

    userScore = 0
    computerScore = 0

    userGuesses = []

    for i in range(0, rounds):
        if i > rounds / 2:
            use_learning(userGuesses)
        computerCoins = random.randint(0, 3)
        userCoins = int(input("How many coins would you like? (0-3)"))
        takingAGuess = True
        userGuess = int(input("How many coins do you think there are?"))
        while takingAGuess:
            computerGuess = random.randint(computerCoins, (6 + (computerCoins - 3)) + 1)
            if not computerGuess == userGuess:
                takingAGuess = False
        if userCoins > 3:
            print("Incorrect input... You lose")
            continue
        guessing = True
        while guessing:
            if computerGuess == (userCoins + computerCoins):
                print("Computer got it")
                computerScore += 1
            else:
                print("Computer got it wrong... But did you?")
            if userGuess < userCoins or userGuess > (6 + (userCoins - 3)):
                userGuess = int(input("THAT ISN'T POSSIBLE, SKRUB! Guess again kiddo "))
            else:
                if userGuess == (userCoins + computerCoins):
                    print("YOU WIN!")
                    userScore += 1
                else:
                    print("Incorrect.... Next round please")
                guessing = False
        userGuesses.append([userGuess, userCoins + computerCoins])

    print("You scored " + str(userScore) + " and the computer scored " +str(computerScore))

except ValueError as e:
    print("You typed a letter where there should have been a number, please restart")
