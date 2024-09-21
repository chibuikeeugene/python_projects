#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""+""+""
firstpart = ''
secondpart = ''
thirdpart = ''
chosen_let = random.sample(letters, nr_letters)
for val in chosen_let:
     firstpart+= val
chosen_sym = random.sample(symbols, nr_symbols)
for val in chosen_sym:
     secondpart+= val
chosen_num = random.sample(numbers, nr_numbers)
for val in chosen_num:
     thirdpart+= val
print(firstpart+secondpart+thirdpart)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
new_list = [firstpart, secondpart, thirdpart]
random.shuffle(new_list)
password = ''
for val in new_list:
     password+= val
print(password)



