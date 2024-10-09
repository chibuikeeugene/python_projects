import auction_art

print("welcome to the secret auction program")
print(auction_art.logo)


bidder_name_and_amount = {} # a dict to hold user name and his bidded amount


user_name = input("what is your name: ")
bidded_amount = input("what is your bid: $")
bidder_name_and_amount[user_name] = bidded_amount



continue_bidding =  True

while continue_bidding:
    additional_bidders = input("Are there any other bidders, type yes or no: \n")
    if additional_bidders == "yes":
        print("\n" * 100) # this line supposedly clears the screen on console
        user_name = input("what is your name: ")
        bidded_amount = input("what is your bid: $")
        bidder_name_and_amount[user_name] = bidded_amount
    else:
        print("\n" * 100) # this line supposedly clears the screen on console
        for key,value in bidder_name_and_amount.items():
            if value == max(bidder_name_and_amount.values()):
                print(f"The winner is {key} with a bid of ${value}")  
            else:
                pass
        continue_bidding = False
        
    



