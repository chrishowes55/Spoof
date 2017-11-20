import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def addToScore(self):
        self.score += 1

    def makeAGuess(self, guess):
        self.guess = guess

    def chooseCoins(self, coins):
        self.coins = coins

try:
    numberOfPlayers = int(input("How many players do you want? "))
    players = []
    for i in range(0, numberOfPlayers):
        name = input("Hello, Player! What should I call you? ")
        players.append(Player(name))


    rounds = int(input("How many rounds would you like to play? "))

    for i in range(0, rounds):
        for j in range(0, len(players)):
            print("Hello, " + players[j].name)
            coins = int(input("How many coins do you have? "))
            players[j].chooseCoins(coins)

            guess = int(input("How many coins do you think there are? "))
            guessing = True
            while guessing:
                print("got to while")
                if j == 0 and not guess < players[j].coins and not guess > (6 - (guess - 3)):
                    guessing = False
                elif j == 0:
                    print("Invalid Guess! That is a silly mistake young person!")
                    guess = int(input("How many coins do you think there are? "))
                else:
                    for k in range(0, j):
                        print("got to for")
                        if players[k].guess == guess or guess < players[j].coins or guess > (6 - (guess - 3)):
                            print("Invalid guess!")
                            guess = int(input("How many coins do you think there are? "))
                        else:
                            print("got to else")
                            guessing = False
                            break
            players[j].makeAGuess(guess)

        for j in range(0, len(players)):
            print("Player " + players[j].name + " guessed " + str(players[j].guess))
            total = 0
            for k in range(0, len(players)):
                total += int(players[k].coins)
            if int(players[j].guess) == total:
                print(players[j].name + " wins!")
                players[j].addToScore()
            else:
                print(players[j].name + " guessed incorrectly!")

    for i in range(0, len(players)):
        print("The score of " + str(players[i].name) + " was " + str(players[i].score))
except ValueError as e:
    print("You typed a letter where there should have been a number, please restart")