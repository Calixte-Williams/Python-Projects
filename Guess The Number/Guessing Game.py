import random

lvl1 = 10
lvl2 = 30
lvl3 = 60
lvl4 = 100
signal = 0

def guess(x):
    answer = random.randint(1, signal)
    guess = 0
    while guess != answer:
        guess = int(input(f'Guess a number between 1 and {signal}: '))
        if guess < answer:
            print('Guess again, you were too low.')
        elif guess > answer:
            print('Guess again, you were too high.')
    print(f'Congrats, you guessed {answer} correclty!!! You Won!!')

print("Welcome to the Guessing Game"
"-----------------------------"
"Guess the correct number and you win... Easy Right!?")
print("Difficulty Levels:" 
"Level 1 = 1 - 10 "
"Level 2 = 1 - 30 "
"Level 3 = 1 - 60 "
"Level 4 = 1 - 100")

difflvl = int(input("Choose your difficulty from 1 to 4: "))  #lets player select the difficulty
if difflvl == 1:
    signal = 10
    guess(signal)
if difflvl == 2:
        signal = 30
        guess(signal)
if difflvl == 3:
        signal = 60
        guess(signal)
else difflvl == 4:
        signal = 100
        guess(signal)


#int(signal)
#print(difflvl)
#print(signal)
#guess(signal)