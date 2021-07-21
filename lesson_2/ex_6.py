from random import randint
import sys

ran_number = randint(1, 100)

for i in range(10):
    g_number = int(input('Enter your guess: ').strip())
    if g_number < ran_number:
        print('Your number is too small')
    elif g_number > ran_number:
        print('Your number is too big')
    else:
        print('You guessed!!!')
        sys.exit()

print(f'10 trials gone...The correct number is {ran_number}')