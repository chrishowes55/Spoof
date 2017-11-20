import random

print("We are going to play spoof!")
userExcited = input("Are you excited? (Y/N) ")
if userExcited == "Y":
    print("YAAAAAY!")
else:
    print("Get good... xD")

rounds = int(input("How many rounds would you like to play? "))

score = 0

for i in range(0, rounds):
    computerCoins = random.randint(0, 3)
    userCoins = int(input("How many coins would you like? (0-3)"))
    if userCoins > 3:
        print("Incorrect input... You lose")
        continue
    guessing = True
    firstTime = True
    while guessing:
        if firstTime:
            userGuess = int(input("How many coins do you think there are in total?"))
            firstTime = False
        elif userGuess < userCoins or userGuess > (6 + (userGuess - 3)):
            userGuess = int(input("THAT ISN'T POSSIBLE, SKRUB! Guess again kiddo (0-3) "))
        else:
            if userGuess == (userCoins + computerCoins):
                print("YOU WIN!")
                score += 1
            else:
                print("Incorrect.... Next round please")
            guessing = False

print("You scored " + str(score) + " out of " + str(rounds))
