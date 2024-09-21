print("Welcome to python pizza deliveries!")
total =  0
pizza_size = input("Enter the size of pizza you want: S, M, L: ")
with_pepperoni = input("Do you want pepperoni? Y or N: ")
withcheese = input("Do you want extra cheese? Y or N: ")

if pizza_size == "S":
    total += 15
    if with_pepperoni == 'Y':
        total+= 2
        if withcheese == 'Y':
            total+=1
            print(f"Your final bill is: ${total}.")
        elif withcheese == 'N':
            print(f"Your final bill is: ${total}.")
    elif with_pepperoni == 'N':
        total
        if withcheese == 'Y':
            total+=1
            print(f"Your final bill is: ${total}.")
        elif withcheese == 'N':
            print(f"Your final bill is: ${total}.")

elif pizza_size == "M":
    total += 20
    if with_pepperoni == 'Y':
        total+= 2
        if withcheese == 'Y':
            total+=1
            print(f"Your final bill is: ${total}.")
        elif withcheese == 'N':
            print(f"Your final bill is: ${total}.")
    elif with_pepperoni == 'N':
        total
        if withcheese == 'Y':
            total+=1
            print(f"Your final bill is: ${total}.")
        elif withcheese == 'N':
            print(f"Your final bill is: ${total}.")


elif pizza_size == "L":
    total += 25
    if with_pepperoni == 'Y':
        total+= 2
        if withcheese == 'Y':
            total+=1
            print(f"Your final bill is: ${total}.")
        elif withcheese == 'N':
            print(f"Your final bill is: ${total}.")
    elif with_pepperoni == 'N':
        total
        if withcheese == 'Y':
            total+=1
            print(f"Your final bill is: ${total}.")
        elif withcheese == 'N':
            print(f"Your final bill is: ${total}.")