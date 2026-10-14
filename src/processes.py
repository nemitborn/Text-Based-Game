import time
import random
import player_stats
import os
import ascii_art

player_stats = player_stats.player_stats
resource_types=["food","ammo","fuel"]

def random_loot(player_stats):  #this function generates and adds random loot, used in a lot of encounters
    supply_loot = random.choice(resource_types) #chooses a random type of resource from resource_types
    supply_amount = random.randint(40, 80)     #chooses a random number in between 40 and 80 to give to the player
    time.sleep(1)
    print("* Inside you find", supply_amount, supply_loot, "*") #notifies the player that they found the loot
    player_stats[supply_loot] += supply_amount      #Adds it to their stats
    time.sleep(1)
    print("+", supply_amount, supply_loot)  #prints a message to notify the player
def clear_screen():
    #clears the screen
    os.system("cls" if os.name == "nt" else "clear")
def merchant_shop(player_stats):    #a separate function for the merchant shop
    print("* The merchant lays out their goods... *")
    time.sleep(1)
    while True: #Always initiates the loop
        print("\n--- Merchant's Shop ---")
        for stat in resource_types:
            print(stat.capitalize(),": ",str(player_stats[stat]))
        print("\nTrade rate: 10 of one resource for 8 of another")      #Like an exchange rate with currencies
        choice = input("What would you like to do?\n 1. Make a trade          2. Leave the shop\n")
        if choice == "1":
            give = input("What do you want to give up? (food, ammo, fuel)\n").lower()   #what the player gives the merchant
            get = input("What do you want in return? (food, ammo, fuel)\n").lower()     #what the player gets from the merchant
            if give not in resource_types or get not in resource_types: #if either option is not in the listed items the player can receive or get
                print("* The Merchant: Aha.. Im afraid I dont have that in stock. But you're welcome to pick something else... *")
                continue    #loops back to the start
            if give == get:
                print("* The merchant laughs at you... *")
                time.sleep(1)
                print("*The Merchant: Aha, a jokester I see. Alright now, lets do some actual trading *")
                continue    #loops back to the start
            if player_stats[give] < 10:  #if the player does not have enough to trade
                print("* You don't have enough ",give," to make that trade... *")
                continue    #loops back to the start

            player_stats[give]-=10
            player_stats[get]+=8
            print("* You trade 10 ",give," for 8 ",get," *")
            time.sleep(1)
        else:
            print("* You thank the merchant and continue on your way... *")
            break
def gameover(player_stats):     #This is a function that checks if the player has less or equal to 0 members in their group
    if player_stats["members"]<=0:  #if the player has 0 or fewer members, else do nothing
        print("* The final member of your group has perished*")
        time.sleep(1)
        print("* You have led your team to their death... *")
        time.sleep(1)
        print(ascii_art.GameOver)
        time.sleep(5)
        print("MEMENTO MORI")       #cool quote
        time.sleep(2)
        exit()  #close the game
def coinFlip():     #The coin flip used in many situations
    coin=["heads","tails"]      #two sides of the coin
    side=random.choice(coin)    #picks a random side
    player_side=input("Choose a side. Heads or Tails?\n>> ")
    player_side=player_side.lower() #turns the player's input into lower case
    if player_side==side:
        return "Pass"

    else:
        return "Fail"
