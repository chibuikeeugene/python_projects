import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ask user is intent for the program
print("Welcome to the Caesar Cipher Program!")
print(art.logo)



def ceaser(
        text, # user text input
        shift_amount, # shift amount
        encode_decode # activity to be performed
        ):
    cipher_text = "" # empty string to store the cipher text
    if encode_decode == "decode":
        shift_amount *= -1
    for letter in text.lower(): # iterate through each letter in the plain text
        if letter not in alphabet:
            cipher_text += letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position > 25:
                new_position = new_position - 26
                new_letter = alphabet[new_position]
            else:
                new_letter = alphabet[new_position]
            cipher_text += new_letter
    # show the result    
    print(f"Here's the {direction}d result: {cipher_text}\n")


game_on = True # variable for continuous looping

while game_on:
    direction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n").lower()
    # retrieve word(s) to be encrypted/decrypted
    text = input("Type your message: \n").lower()
    # retrieve intended shift or adjustment criteria number
    shift = int(input("Type the shift number: \n"))
    # call the function
    ceaser(text=text, shift_amount=shift, encode_decode=direction)

    is_user_still_interested = input("Would you like to continue, type yes or no: \n")
    if is_user_still_interested == "no":
        game_on = False
        print("Thank you for using the Caesar Cipher Program!")
    else:
        continue






# Initial Granualar code logic

# # encryption function block
# def encrypt(plain_text:str, shift_amount:int):
#     cipher_text = "" # empty string to store the cipher text
    
#     for letter in plain_text.lower(): # iterate through each letter in the plain text
#         if letter == ' ':
#             cipher_text += ' '
#             continue
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         if new_position > 25:
#             new_position = new_position - 26
#             new_letter = alphabet[new_position]
#         else:
#             new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")

# # decryption function block
# def decrypt(plain_text:str, shift_amount:int):
#     cipher_text = ""

#     for letter in plain_text:
#         if letter == ' ':
#             cipher_text += ' '
#             continue
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         if new_position > 25:
#             new_position = new_position - 26
#             new_letter = alphabet[new_position]
#         else:
#             new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text.capitalize()}")

    
# if direction == "encode":
#     encrypt(plain_text= text, shift_amount = shift)
# elif direction == "decode":
#     decrypt(plain_text= text, shift_amount = shift)
# else:
#     pass

