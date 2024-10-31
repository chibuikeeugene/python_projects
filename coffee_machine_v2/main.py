from menu_and_resources import Menu, MenuItem
from coffee_maker_logic import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker() #  create a coffemaker object
money_machine =  MoneyMachine() # create a money machine object
menu = Menu()

# TODO: 1. Generate report
coffee_maker.report()
money_machine.report()

continue_processing_drinks =  True


while continue_processing_drinks:

    # TODO: 2. Check resources is sufficient
    user_prompt = input('what drink would you like today - espresso, latte, cappuccino: ').lower()

    items = menu.get_items() # get all available drink items 

    # check if user prompt exists in the menu
    if user_prompt in items:

        drink_item = menu.find_drink(user_prompt) # retrieve drink attributes - name, water, milk, cost ...
        
        resource_response = coffee_maker.is_resource_sufficient(drink=drink_item)

        if resource_response: # if true

            # TODO: 3. Process coins
            drink_item_cost = drink_item.cost # retrieves the drink cost from the system
            is_payment_accepted = money_machine.make_payment(cost=drink_item_cost) # compares money received with the system cost of the item

            # TODO: 4. Check that transaction is successful
            if is_payment_accepted: # if true

                # TODO: 5. Make the coffee
                coffee_maker.make_coffee(order=drink_item)

    elif user_prompt == 'off':
        continue_processing_drinks = False
        print('Shutting down the machine...')

    elif user_prompt == 'report':
        coffee_maker.report()
        money_machine.report()
        continue_processing = True