# Fun guessing game where the computer guesses the number you think of in your mind and guesses it. Beware, computers are taking over! 
# As part of a beginer fun python project


import random

def cpu_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high(h) or too low(l) or correct(c) ??: ' ).lower()
        if feedback in ('l','h','c'):
            if feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1
        else:
            print('Invalid selection. Choose from high(h) or low(l) or correct(c)')
    print(f'Yay! The computer guessed right. Your number is: {guess}')

print('Think of a number between 1 and 10 and the computer will try to guess it!.')
start = input('Hit (y) to continue and (n) to stop: ').lower()
 
if start == 'y':
    cpu_guess(10)
elif start == 'n':
    print('ok, sayonnara')
    exit()
elif start not in ('y','n'):
    print('Invalid selection. Choose from Yes(y) or No(n) to play.')
    exit()