import cal_logo
print(cal_logo.logo)


# addition block
def add(n1, n2):
    return n1 + n2

# multiplication block
def multiply(n1, n2):
    return n1 * n2

# substraction block
def subtract(n1, n2):
    return n1 - n2

# division block
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

result = 0

# handles numerical calculation
def calculation(op, num1, num2):
    if op in operations.keys():
        result = operations[str(op)](num1, num2)
        return result
    
# handles continuous request
def continue_user_request():
    print(" + \n * \n - \n / \n ") # show user the available maths operator
    # request the operator from the user
    operator =  input('type in a mathematical operator: ')
    # request the second number from user
    new_number = float(input("what is the next number: "))
    return operator, new_number

# handles first request
def user_input():
    # request first number from user
    f_number = float(input("enter the first number: "))

    print(" + \n * \n - \n / \n ") # show user the available maths operator

    # request the operator from the user
    opr =  input('type in a mathematical operator: ')

    # request the second number from user
    s_number = float(input("what is the next number: "))

    return opr, f_number, s_number


operator, first_number, second_number = user_input()

result =  calculation(op=operator, num1=first_number, num2=second_number)
print(result)

continue_calculation = True # a variable for continuous looping

while continue_calculation:
    user_response = input(f'would you like to continue calcu. with {result}, if so, enter yes, else no, to start a new calculation, or type exit: ').lower()

    if user_response == 'yes':
        new_op, new_num = continue_user_request()
        result = calculation(op=new_op, num1=result, num2=new_num)
        print(result)


    elif user_response == 'no':
        continue_calculation = False
        print('\n' * 100) # clear the screen
        print('starting a new calculation...')
        opr, f_number, s_number= user_input()
        result = calculation(op=opr, num1=f_number, num2= s_number)
        print(result)
        continue_calculation = True

    else:
        continue_calculation = False
        print('Thanks for using my calculator')



