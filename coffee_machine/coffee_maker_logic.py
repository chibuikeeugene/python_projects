from menu_and_resources import menu, resources

coffee_options = ['expresso', 'latte', 'cappuccino']
current_earnings = 0
resources_left = resources




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
    q = int(input('quarters: '))
    d = int(input('dimes: '))
    n = int(input('nickles: '))
    p = int(input('pennies: '))
    monetary_value  = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
    print(f'Total coins amount to: ${round(monetary_value, 2)}')
    return monetary_value


#TODO: 6. Check transaction successful?
def is_transaction_successful(user_coins: float, choice: str) -> str:
    
    if user_coins > menu[choice]['costs']:
        change =  user_coins - menu[choice]['costs']
        print(f'Here\'s your change: ${change}')
        return 'yes'
    elif user_coins == menu[choice]['costs']:
        print(f'You have ${change} change')
        return 'yes'
    else:
        return "No"
    

continue_processing =  True
while continue_processing:
    #TODO : 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    user_choice = input("What would you like? (expresso/latte/cappuccino): ").lower()#TODO : 2. Turn off the Coffee Machine by entering “ off ” to the prompt.

    if user_choice == 'off':
        continue_processing = False
        print('Shutting down the machine...')

    #TODO: 3. Print report.
    if user_choice == 'report':
        print(f'Water: {resources_left['water']}ml\nMilk: {resources_left['milk']}ml\nCoffee: {resources_left['coffee']}g\nMoney: ${current_earnings}')
        continue_processing = True

    if user_choice in coffee_options:
        ingredients = menu[user_choice]['ingredients']
        
        # check if the resources is sufficient
        resource_response = is_resource_sufficient(client_request= ingredients, system_resources=resources_left)

        if resource_response == 'yes':
            # process payment
            payment_result = process_payment()
            # check if the payment is sufficient for the drink
            transaction_response = is_transaction_successful(payment_result, choice= user_choice )
            if transaction_response == 'yes':
                # add the costs of the drink to the machine as the profits
                current_earnings += menu[user_choice]['costs']

                # subtract the ingredients used in making the drink from the machine's resources
                resources_calculation = {key: resources_left[key] - menu[user_choice]['ingredients'][key] for key in resources_left}
                resources_left = resources_calculation

                #TODO: 7. Make Coffee.
                print(f'Here is your {user_choice} ☕️. Enjoy!')
                continue_processing = True
            else:
                continue_processing = False
                print('Insufficient amount. Money refunded!')
        else:
            continue_processing = False
            print(resource_response)
    
