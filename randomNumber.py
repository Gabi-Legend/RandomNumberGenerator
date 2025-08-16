import random

print("welcome to random number generator!")
print("Your job is to find the generated number in less than 5 tries!")
play = input("Do you want to play?(Y/N) : ").lower()

def playGame():
    guessed = False
    guesses = 0
    randomNumber = random.randint(1,10)
    while guesses < 5:
        yourGuess = int(input("Your guess : "))
        if(yourGuess == randomNumber):
            guessed = True
            guesses+=1
            print(f"Congrats, you guesses the number in {guesses} tries!")
            break
        else:
            print("Try again")
            guesses+=1
    if guessed == False:
        print("You lost!")

def quit():
    print("Maybe later!")

if play == "yes" or play == "da" or play == "y":
    playGame()
else:
    quit()