import random

print("Welcome to the Mastermind Game!")
secretNumber = random.randint(1000, 10000)
guess = int(input("Guess the 4 digit number : "))
print()
print()

if guess == secretNumber:
    print("Great! You just guessed the number in your first try ! You are a Mastermind!")
else:
    tries = 0
    while guess != secretNumber:
        tries += 1
        secretNumber = str(secretNumber)
        guess = str(guess)

        count = 0
        correctGuess = ["X", "X", "X", "X"]
        for i in range(0, 4):
            if guess[i] == secretNumber[i]:
                count += 1
                correctGuess[i] = guess[i]
            else:
                continue
        if count < 4 and count != 0:
            print(f"Nope! But you did get {count} digits correct!")
            print("Also these numbers in your input were correct.")
            for k in correctGuess:
                print(k, end='')
            print('\n')
            guess = int(input("Enter your next choice of numbers : "))
        elif count == 0:
            print("None of the numbers in your input match.")
            guess = int(input("Enter your next choice of numbers: "))

if guess == secretNumber:
    print("You've become a Mastermind!")
    print("It took you only " + str(tries) + " tries.")
