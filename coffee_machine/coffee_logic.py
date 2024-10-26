from menu_and_resources import menu, resources

coffee_options = ['espresso', 'latte', 'cappuccino']
current_earnings = 100
resources_left =  resources

continue_processing =  True



#TODO : 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

#TODO : 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
if user_choice == 'off':
    pass

#TODO: 3. Print report.
if user_choice == 'report':
    print(f'Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${current_earnings}')

#TODO: 4. Check resources sufficient?
def is_resource_sufficient(client_request: dict, system_resources: dict) -> str:
    if client_request['water'] <= system_resources['water']:
        if client_request['milk'] <= system_resources['milk']:
            if client_request['coffee'] <= system_resources['coffee']:
                return 'yes'
            else:
                return 'Insufficient coffee to make drink'
        else:
            return 'Insufficient milk to make drink'
    else:
        return 'Insufficient water to make drink'

#TODO: 5. Process coins.
def process_payment() -> float:
    print('please insert coins: \n')
    q = int(input('quarters: \n'))
    d = int(input('dimes: \n'))
    n = int(input('nickles: \n'))
    p = int(input('pennies: \n'))
    monetary_value  = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
    print(f'Total coins provided: ${monetary_value}')
    return monetary_value


#TODO: 6. Check transaction successful?
def is_transaction_successful(user_coins: float, user_choice: str) -> str:
    
    if user_coins >= menu[user_choice]['costs']:
        pass
    else:
        return "Insufficient amount"


if user_choice in coffee_options:
    ingredients = menu[user_choice]['ingredients']
    
    # check if the resources is sufficient
    response = is_resource_sufficient(client_request= ingredients, system_resources=resources)

    if response == 'yes':
        # process payment
        result = process_payment()

        pass
    else:
        print(response)
else:
    print(f"KeyError: {user_choice} - The key '{user_choice}' does not exist in the dictionary.")






#TODO: 7. Make Coffee.