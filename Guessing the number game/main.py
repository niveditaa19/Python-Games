import random

print("Welcome to Guessing the Number Game!")
lower = int(input("Enter the starting range : "))
upper = int(input("Enter the ending range : "))
secretNumber = random.randint(lower, upper)

for i in range(7):
    guess = int(input("Take a guess..."))
    if guess == secretNumber:
        print(f"Yay! You Win! You guessed the Right Number : {secretNumber} ")
        break
    elif guess > secretNumber:
        print("Your guess is too high...Try again!")
    elif guess < secretNumber:
        print("Your guess is too low...Try again!")

if guess != secretNumber:
    print(f"Nope. You Lose! The number is : {secretNumber}")
