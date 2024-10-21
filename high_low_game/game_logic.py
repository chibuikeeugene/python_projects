import art
from game_data import influencers
from random import randint


def actor_with_the_most_followers(index1: int, index2: int):
    """ this function block returns the assigned letter of the actor with the most followers"""

    print(f'Compare A: {influencers[index1]['name']},{influencers[index1]['short_description']},{influencers[index1]['country']}')
    
    print()

    print(art.vs)
    
    if index2 != 50:
        print(f'Compare B: {influencers[index2]['name']},{influencers[index2]['short_description']},{influencers[index2]['country']}')
    else:
        index2 = 0
        print(f'Compare B: {influencers[index2]['name']},{influencers[index2]['short_description']},{influencers[index2]['country']}')
        
    if influencers[index1]['Instagram_follower_count'] > influencers[index2]['Instagram_follower_count']:
        return 'A'
    else:
        return 'B'


def compare_user_answer(user_answer:str, system_answer:str):

    current_score = 0
    
    """this function block validates user's answer to either correct or wrong and returns the user's current score"""
    if user_answer == system_answer:
        current_score +=1
        return current_score
    else:
        return current_score
        
actor_a = randint(0, 49)

continue_game = True

final_score = 0

while continue_game:
    print(art.logo)

    actor_b = actor_a + 1

    system_response = actor_with_the_most_followers(actor_a, actor_b) # obtain system's

    user_input = input('who has more followers. Type A or B: ').capitalize()

    score = compare_user_answer(user_answer=user_input, system_answer=system_response)

    final_score+=score

    if user_input != system_response:
        print(f'Sorry, that\'s wrong. Final score: {final_score}')
        continue_game = False
    else:
        actor_a =  actor_b
        print(f'You are right, current score: {final_score}.')




    







