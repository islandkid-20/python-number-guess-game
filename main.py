import random


def number_gues_game():
    hidden_number = random.randint(1,10)
    attemps = 3

    print('===> Welcome to the Number Gues Game <====')
    print('===> Please Gues any number between 1 to 10 to get an hidden number. <====')
    print('====> You have 3 attemps <====')

    while attemps > 0:
        try:
            guess = int(input(f'Enter your guess number (Attemp {4 - attemps} / 3): '))

            if guess < 1 or guess > 10:
                print('Please enter a valid number between 1 and 10.')
                continue
            if guess == hidden_number:
                print('Congulaturations!. You have guessed the correct number and won the game.')
                return;
            
            else:
                attemps -= 1
                print('Incorrect guess')
                if attemps > 0:
                    print(f'Try again. You have {attemps} left.')
        except ValueError:
            print('Invalid  input. Please enter a valid number between 1 and 10.')

    print(f'Sorry you have used all attemps the correct hidden number was {hidden_number}')

# Function call
number_gues_game()