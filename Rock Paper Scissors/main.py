import random

print("winning Rules of the Rock paper and scissor game as follows:")
print("rock vs paper->paper wins")
print("rock vs scissors->rock wins")
print("paper vs scissors->scissors wins")

options = ["Rock", "Paper", "Scissor"]
computer = random.choice(options)
a = True
while a:
    choice = input("Choose one : Rock, Paper or Scissor : ")
    print(f"You chose {choice}")
    print()
    print()
    print("Now it's the Computer's turn.....")
    print()
    print()
    print(f"Computer's choice is : {computer}")
    if computer == "Rock" and choice == "Paper":
        print("Rock Vs Paper, You Win!")
    elif computer == "Paper" and choice == "Scissor":
        print("Paper Vs Scissor, You Win!")
    elif computer == "Scissor" and choice == "Rock":
        print("Scissor Vs Rock, You Win!")
    elif computer == "Rock" and choice == "Rock":
        print("Rock Vs Rock, It's a Draw!")
    elif computer == "Paper" and choice == "Paper":
        print("Paper Vs Paper, It's a Draw!")
    elif computer == "Scissor" and choice == "Scissor":
        print("Scissor Vs Scissor, It's a Draw!")
    elif computer == "Paper" and choice == "Rock":
        print("Paper Vs Rock, Computer Wins!")
    elif computer == "Scissor" and choice == "Paper":
        print("Scissor Vs Paper , Computer Wins!")
    elif computer == "Rock" and choice == "Scissor":
        print("Rock Vs Scissor , Computer Wins!")

    b = input("Do you wanna play again?[Y/N]")
    if b == "N":
        a = False
