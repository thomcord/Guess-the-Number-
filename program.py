# Simple project that will ask the user to guess a number.

print('-----------------------')
print('-----Guessing Game-----')
print('-----------------------')
print('In this game you have to try to guess a secret number from 0 to 20. You have 3 guesses. Good Luck!')

secretNumber = 7
numberOfTries = 3
round = 1

while (round <= numberOfTries):
    print('Try {} from {}' .format(round, numberOfTries))
    guess = int(input('Enter a numbe:'))
    print('You entere:', guess)
    
    right = guess == secretNumber
    bigger = guess > secretNumber
    smaller = guess < secretNumber
    
    if (right):
        print('Congratulations! You have entered the right number')
        break
    elif (bigger):
        print('Wrong number! Your guess is higher then the secret number')
    elif(smaller):
        print('Wrong number! Your guess is lower then the secret number ')
        
        round = round +1
        
print('End of the game!')