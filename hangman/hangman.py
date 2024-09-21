import hangman_art
import hangman_words



# show users a welcoeme page
print(hangman_art.welcome_screen)

placeholder = '' # a variable to count the exact number of a word

stages = hangman_art.stages

user_input = input("Enter a word that exists in my list: ").capitalize() # request user input
if user_input not in hangman_words.word_list: # check if user input is in the list
    print('Word not found in the list')
else:
    length_of_word = len(user_input)

    for value in range(length_of_word): # 
        placeholder += '_'

    print('your word is: ' + user_input)
    print('Here\'s a placeholder for your word: ' + placeholder)

    word_status = []

    game_over =  False

    lives =  6 # number of lives a user has

    while not game_over:

        guess = input('guess a letter in the word: ')

        display_status = ''

        if guess in word_status:
            print(f'You have already guessed the letter -  {guess}')

        if guess not in user_input:
            lives-= 1
            print('You have '+ str(lives) + ' lives left after making a wrong guess')

        for letter in user_input:
            if letter == guess:
                display_status+= letter
                word_status.append(guess)
            elif letter in word_status:
                display_status+= letter
            else:
                display_status+= '_'
        
        print('Current word update: '+ display_status)
        if display_status == user_input:
            game_over = True
            print('You won!')

        elif lives == 0:
            game_over = True
            print('No more lives, You lost!')
        

        print(stages[lives])

    

    