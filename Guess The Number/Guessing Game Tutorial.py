import random    #Import this module that implements pseudo-random number generators for various distributions.

def guess(x):    #Define a Function
    random_number = random.randint(1, x)  #Use random.randint() module to generate number for varible random_number
    guess = 0                             #Sets guess to equal 0, out of the range of the random.randint(1, X) range
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))   #Sets variable as int
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Congrats, you have guessed {random_number} correctly. You Won!!')

guess(10)     #Define the number for Guess