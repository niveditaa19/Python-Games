import random

words = ['rainbow', 'computer', 'data', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'keyboard', 'table']

secretWord = random.choice(words)
name = input("What is your name? : ")
print(f"Good Luck, {name}!")
print('\n')
print("Guess the Characters of the Secret Word :\n ")
correctWord = ''
for i in correctWord:
    print(i, end='')
turns = 15
while turns > 0:
    fails = 0
    for k in secretWord:
        if k in correctWord:
            print(k, end='')
        else:
            print('_', end='')
            fails += 1
    if fails == 0:
        print("\nYou Win!")
        print(f"The Word is : {secretWord} ")
        break
    print()
    guess = input("\nGuess a Character : ")
    correctWord += guess
    if guess not in secretWord:
        turns -= 1
        print(f"Wrong! You only have {turns} left")
        if turns == 0:
            print(f"You Lose!! The Word was {secretWord}")
