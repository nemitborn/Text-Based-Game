import time
import random
import inventory
import os
import ascii_art
from playsound3 import playsound


current_stats=inventory.player_stats
resource_types=["food","ammo","fuel"]

def random_loot(current_stats):  #this function generates and adds random loot, used in a lot of encounters
    supply_loot = random.choice(resource_types) #chooses a random type of resource from resource_types
    supply_amount = random.randint(40, 80)     #chooses a random number in between 40 and 80 to give to the player
    time.sleep(1)
    print("* Inside you find", supply_amount, supply_loot, "*") #notifies the player that they found the loot
    current_stats[supply_loot] += supply_amount      #Adds it to their stats
    time.sleep(1)
    print("+", supply_amount, supply_loot)  #prints a message to notify the player
def clear_screen():
    #clears the screen
    os.system("cls" if os.name == "nt" else "clear")
def gameover(current_stats):     #This is a function that checks if the player has less or equal to 0 members in their group
    if current_stats["members"]<=0:  #if the player has 0 or fewer members, else do nothing
        print("* The final member of your group has perished*")
        time.sleep(1)
        print("* You have led your team to their death... *")
        time.sleep(1)
        print(ascii_art.GameOver)
        time.sleep(1)
        input("Press enter to continue...")
        clear_screen()
        print(ascii_art.GameOver_quote)       #cool quote
        time.sleep(5)
        clear_screen()
        print(ascii_art.skulls)
        playsound("sounds/storm.mp3")
        exit()  #close the game
def coinFlip():
    coin=["heads", "tails"]
    side=random.choice(coin)
    player_side=input("Choose a side. Heads or Tails?\n>> ").lower().strip()
    time.sleep(1)
    #if the player types "head", this function automatically adds the s at the end to turn it into "heads"
    if player_side in ["head", "tail"]:
        player_side+="s"
    #checks if the side the player chose matches to the side the player
    print("* The coin landed on", side, "*")
    time.sleep(1)
    if player_side==side:
        return "Pass"
    else:
        return "Fail"


#SHOPS
def merchant_shop(current_stats):    #a separate function for the merchant shop
    print("* The merchant shows you their goods... *")
    time.sleep(1)
    while True: #Always initiates the loop
        print("\n--- Merchant's Shop ---")
        for stat in resource_types:
            print(stat.capitalize(),": ",str(current_stats[stat]))
        print("\nTrade rate: 10 of one resource for 8 of another")      #Like an exchange rate with currencies
        while True:
            try:
                choice = int(input("What would you like to do?\n 1. Make a trade          2. Leave the shop\n>> "))
                if choice == 1 or choice == 2:
                    break
                else:
                    print("* Please pick a number between 1 and 2. *")
            except ValueError:
                print("* That is not a number, try again. *")
        if choice==1:
            give = input("What do you want to give up? (food, ammo, fuel)\n").lower()   #what the player gives the merchant
            get = input("What do you want in return? (food, ammo, fuel)\n").lower()     #what the player gets from the merchant
            if give not in resource_types or get not in resource_types: #if either option is not in the listed items the player can receive or get
                print("The Merchant: Aha.. Im afraid I dont have that in stock. But you're welcome to pick something else... ")
                continue    #loops back to the start
            if give == get:
                print("* The merchant laughs at you... *")
                time.sleep(1)
                print("The Merchant: Aha, a jokester I see. Alright now, lets do some actual trading")
                continue    #loops back to the start
            if current_stats[give] < 10:  #if the player does not have enough to trade
                print("* You don't have enough ",give," to make that trade... *")
                continue    #loops back to the start
            current_stats[give]-=10
            current_stats[get]+=8
            print("* You trade 10 ",give," for 8 ",get," *")
            time.sleep(1)
        elif choice==2:
            print("* You thank the merchant and continue on your way... *")
            break
        else:
            print("The Merchant: Aha... I didn't understand that. Well I'll be on my way now.")
            break
def butcher_shop(current_stats):
    print("* The butcher lays out their goods... *")
    time.sleep(1)
    while True:
        #prints out all the player's current stats that can be traded
        for stat in resource_types:
            print(stat.capitalize(), ": ", str(current_stats[stat]))
        time.sleep(1)
        print("\nTrade rate: 10 of one item for 8 food")
        time.sleep(1)
        while True:
            try:
                choice = int(input("What would you like to do?\n 1. Trade for food          2. Recruit the butcher          3. Leave\n"))
                if choice==1 or choice==2:
                    break
                else:
                    print("* Please pick a number between 1 and 2. *")
            except ValueError:
                print("* That is not a number, try again. *")
        if choice==1:
            give=input("What do you want to give up? (ammo, fuel)\n").lower()
            time.sleep(1)
            if give not in ["ammo","fuel"]:
                print("The Butcher: I only take ammo or fuel for my food. *")
                time.sleep(1)
                continue
            if current_stats[give]<10:
                time.sleep(1)
                print("* You don't have enough",give,"to make that trade... *")
                time.sleep(1)
                continue
            current_stats[give]-=10
            current_stats["food"]+=8
            print("* You trade 10 ",give," for 8 food *")
            time.sleep(1)
        elif choice==2:
            if coinFlip()=="Pass":
                print("PASS")
                time.sleep(1)
                print("* You ask the butcher if he wants to join your journey. *")
                time.sleep(1)
                print("The Butcher: Beats staying out here alone. Alright, I'll join you.")
                time.sleep(1)
                current_stats["members"]+=1
                print("+1 member")
                time.sleep(1)
                break
            else:
                print("FAIL")
                time.sleep(1)
                print("* You ask the butcher if he wants to join your journey. *")
                time.sleep(1)
                print("The Butcher: Eh... I'm good, I wish you well on your travels")
                break
        elif choice==3:
            print("The Butcher: Eh? speak up.")
            continue
        else:
            print("* You thank the butcher and continue on your way... *")
            break
gameover(current_stats)
