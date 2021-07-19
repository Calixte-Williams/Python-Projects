import random    #Import this module that implements pseudo-random number generators for various distributions.

def guess(x):    #Define a Function
    random_number = random.randint(1, x)  #Use random.randint() module to generate number for varible random_number
    guess = 0                             #Sets guess to 0, out of the range of the random.randint(1, X) range, simply to initialize Guess Variable
    while guess != random_number:        # " != " means not equal to
        guess = int(input(f"Guess a number between 1 and {x}: "))   #Sets variable as int
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Congrats, you have guessed {random_number} correctly. You Won!!')

guess(10)     #Calls on the defined function to begin and tells it the highest number to use

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'h':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')

computer_guess(10)