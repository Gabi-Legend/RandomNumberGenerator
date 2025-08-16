import random

print("welcome to random number generator!")
print("Your job is to find the generated number in less than 5 tries!")
input("Do you want to play?(Y/N) : ").lower()

def play():
    guessed = False
    guesses = 0
    randomNumber = random.randint(1,10)
    while guesses < 5:
        yourGuess = int(input("Your guess : "))
        if(yourGuess == randomNumber):
            guessed = True
            print("Congrats, you guesses the number!")
            break
    if guessed == False:
        print("You lost!")

def quit():
    print("Maybe later!")