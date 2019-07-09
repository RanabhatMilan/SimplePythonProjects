# This is a simple guessing game.
# At first we import a inbuilt library to use a function to generate some random numbers
import random

def guess_num(total):
    number = random.randint(1, 10)
    num = int(input("Guess a number between 1 to 10: "))
    while num != number:
        if num > number:
            num = int(input("Guess a number lower than "+str(num)+"! Try Again: "))
        if num < number:
            num = int(input("Guess a number higher than "+str(num)+"! Try Again: "))
    if num == number:
        yn = input("Ohh..Your guess is Correct. \nYou WIN. Your total score is "+str(total)+". Do you want to play Again?[y/n] ")
        return yn

name = input("What's your name? ")
yn = input("Hello "+name+"!! Do you want to play some game?[y/n]")
total = 10
while yn == 'y':
    yn = guess_num(total)
    total += 10
if yn == 'n':
    print ("Okaay.. Cool")
