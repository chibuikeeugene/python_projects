#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# read the starting letter file
with open('/Users/eugene/Personal_Projects/python_projects/mail_merge/Input/Letters/starting_letter.txt', mode='r') as fin:
    contents = fin.read()

# read the invited names file
with open('/Users/eugene/Personal_Projects/python_projects/mail_merge/Input/Names/invited_names.txt', mode='r') as f:
    receipients = f.readlines()

# loop over the invited names and append their names on the starting letter and save each copy in the ready to send folder
for names in receipients:
    updated_content = contents.replace('[name]', f'{names}')
    with open(f'/Users/eugene/Personal_Projects/python_projects/mail_merge/Output/ReadyToSend/letter_for_{names}', mode= 'w+') as fout:
        fout.write(updated_content)