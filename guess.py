import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

#Ask player to guess 6 times

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Too low')
    elif guess > secretNumber:
        print('Too high')
    else:
        break
if guess == secretNumber:
    print("Correcto, you've guessed it right in " + str(guessesTaken) + ' gusses')
else:
    print('Nope, the number I had in mind was ' + str(secretNumber))
