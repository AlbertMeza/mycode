#!/usr/bin/env python3

import random

"""
The incremental bot's airship, USER_ERROR, has begun an all-out attack on the TLG cohort. It must be destroyed or the cohort 
will have to join the military again. Only by combining the knowledge taught by Chad, Nick, Nelly, and Donte along with your
programming skills does the cohort stand a chance.

RULES:
1) The game starts with the python bot establishing themselve within the city coordinates of 0-100 INCLUSIVE
2) Then the program allows YOU to guess repeatedly where this bot has been set within the city 
3) You take 1 hp of damage every turn that the bot survives  whereas the damage you deal depends on the chart below
    
    Most turns one 1 hp of damage is dished out 
    Turns that are multiples of 3 are FIRE Damage which is 3 hp of damage
    Turns that are multiples of 5 are ELECTRIC damage which is 3 hp of damage
    Turns that are multiples of 3 AND 5 are BOTH FIRE AND ELECTRIC damage
        which is 10 hp of damage 

 *during every turn you'll see a current status(round number, user hp, python bot hp)*


                                SAMPLE DISPLAY

STATUS: Round 6 User: 10/15 USER_ERROR: 3/10
Your TEMUX is expected to deal 3 damage this round
Enter desired coordinate to inspect: 32 <- user inputted
.....
YOU FOUND THE BOT
THE USER_ERROR HAS BEEN DESTROYED! You will not have to reeenlist

"""


#method to start play
def main(): 
    #Set the healths and round counter
    USER_ERROR = 15
    user = 16
    round = 1
    reposition = 1

    bot_position = random.randint(0,101) #set up bot coordinate
    while user > 0 and USER_ERROR > 0:
        if reposition == 1 and USER_ERROR < 7: #logic to reposition bot when at half health
            print("==============================================")
            print("Incremental bot has repositioned!!!")
            reposition -= 1
            bot_position = random.randint(0,101)
        print("==============================================")
        print(f"STATUS: Round: {round} user HP: {user}/16 USER_ERROR HP: {USER_ERROR}/15")
        damage = 1

        #logic to calculate damage
        if round % 5 == 0 and round % 3 == 0:
            damage = 10;
        elif round % 5 == 0 or round % 3 == 0:
            damage = 3;
        print(f"Your TEMUX attack is expected to deal {damage} damage this round")

        target_coordinate = 0

        try:
            target_coordinate = int(input("Enter the desired target coordinate(0-100): "))
        except:
            print("you fail for not following instructors, the increment was correct....")
            print("USER_ERROR!!")
        #logic to calucalute positioning vs guess
        if target_coordinate < bot_position:
            print("The TEMUX attack FELL SHORT of the bot's positioning")
        elif target_coordinate > bot_position:
            print("The TEMUX attack OVERSHOT the bot's positioning")
        else:
            print("The TEMUX attack was a DIRECT HIT!")
            USER_ERROR -= damage
            
        #logic after a round is complete    
        if USER_ERROR > 1:
            user -= 1;
            round +=1
    
    #end state logic
    print("==============================================")
    if USER_ERROR < 1:
        print("Congratulations, you have saved TLG cohort and destroyed the incremental bot")
    else:
        print("Army recruiters are coming your way")
main()



