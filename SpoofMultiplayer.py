import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def addToScore():
        score += 1

    def makeAGuess(guess):
        self.guess = guess

    def chooseCoins(coins):
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
