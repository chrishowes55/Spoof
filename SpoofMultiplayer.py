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

numberOfPlayers = int(input("How many players do you want?"))
players = []
for i in range(0, numberOfPlayers):
    name = input("Hello, Player! What should I call you?")
    players.append(Player(name))
    

rounds = int(input("How many rounds would you like to play? "))

for i in range(0, rounds):
    for j in range(0, len(players)):
        print("Hello, " + players[j].name)
        coins = input("How many coins do you have?")
        players[j].chooseCoins(coins)
        
        guess = input("How many coins do you think there are?")
        players[j].makeAGuess(guess)

    for j in range(0, len(players)):
        print("Player " + players[j].name + " guessed " + players[j].guess)
        total = 0
        for k in range(0, len(players)):
            total += int(players[k].coins)
        if int(players[j].guess) == total:
            print(players[j].name + " wins with " + str(players[j].guess) + "!")
            players[j].addToScore()
        else:
            print(players[j].name + " guessed incorrectly with " + str(players[j].guess))

for i in range(0, len(players)):
    print("The score of " + str(players[i].name) + " was " + str(players[i].score))
