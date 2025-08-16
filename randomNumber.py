import random

print("Welcome to random number generator!")
print("Your job is to find the generated number in less than 5 tries!")
play = input("Do you want to play? (Y/N): ").lower()

def playGame():
    guessed = False
    guesses = 0
    randomNumber = random.randint(1, 10)
    
    while guesses < 5:
        try:
            yourGuess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        guesses += 1
        if yourGuess == randomNumber:
            guessed = True
            print(f"Congrats, you guessed the number in {guesses} tries!")
            break
        elif yourGuess < randomNumber:
            print("Too low, try again.")
        else:
            print("Too high, try again.")

    if not guessed:
        print(f"You lost! The number was {randomNumber}.")

def exitGame():
    print("Maybe later!")

if play in ["yes", "da", "y"]:
    playGame()
else:
    exitGame()
