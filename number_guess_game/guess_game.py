import art
import random


print(art.logo)
# result = 0

print("I am thinking of a number between 1 and 100 \n")
result = random.randint(1, 100)  # computer held value to be compared with user input
print(result)

level = input('Choose a difficulty level: Type "easy" or "hard":')



number_of_attempts_easy = 10
number_of_attempts_hard = 5

continue_game = True

if level == 'easy':
    print(f'you have {number_of_attempts_easy} attempts remaining to guess the number')
    while continue_game:
        user_guess = int(input('make a guess: '))
        if user_guess == result:
            print('you win, that is the correct answer')
            continue_game = False
        else:
            if user_guess < result:
                print('too low\nguess again\n')
            elif user_guess > result:
                print('too high\nguess again\n')
            number_of_attempts_easy -= 1
            print(f'you have {number_of_attempts_easy} attempts remaining to guess the number')
            continue_game = True
            if number_of_attempts_easy == 0:
                print('you lose, do you want to retry...')
                continue_game = False
    
elif level == 'hard':
    print(f'you have {number_of_attempts_hard} attempts remaining to guess the number')
    while continue_game:
        user_guess = int(input('make a guess: '))
        if user_guess == result:
            print('you win, that is the correct answer')
            continue_game = False
        else:
            if user_guess < result:
                print('too low\nguess again\n')
            elif user_guess > result:
                print('too high\nguess again\n')
            number_of_attempts_hard -= 1
            print(f'you have {number_of_attempts_hard} attempts remaining to guess the number')
            continue_game = True
            if number_of_attempts_hard == 0:
                print('you lose, do you want to retry...')
                continue_game = False

else:
    print('invalid level chosen')