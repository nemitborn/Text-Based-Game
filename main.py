import time
import random
titleCard="""
    ███        ▄█    █▄       ▄████████       ▄█     █▄   ▄█  ███▄▄▄▄       ███        ▄████████    ▄████████         ▄████████  ▄██████▄     ▄████████ ████████▄  
▀█████████▄   ███    ███     ███    ███      ███     ███ ███  ███▀▀▀██▄ ▀█████████▄   ███    ███   ███    ███        ███    ███ ███    ███   ███    ███ ███   ▀███ 
   ▀███▀▀██   ███    ███     ███    █▀       ███     ███ ███▌ ███   ███    ▀███▀▀██   ███    █▀    ███    ███        ███    ███ ███    ███   ███    ███ ███    ███ 
    ███   ▀  ▄███▄▄▄▄███▄▄  ▄███▄▄▄          ███     ███ ███▌ ███   ███     ███   ▀  ▄███▄▄▄      ▄███▄▄▄▄██▀       ▄███▄▄▄▄██▀ ███    ███   ███    ███ ███    ███ 
    ███     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀          ███     ███ ███▌ ███   ███     ███     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀        ▀▀███▀▀▀▀▀   ███    ███ ▀███████████ ███    ███ 
    ███       ███    ███     ███    █▄       ███     ███ ███  ███   ███     ███       ███    █▄  ▀███████████      ▀███████████ ███    ███   ███    ███ ███    ███ 
    ███       ███    ███     ███    ███      ███ ▄█▄ ███ ███  ███   ███     ███       ███    ███   ███    ███        ███    ███ ███    ███   ███    ███ ███   ▄███ 
   ▄████▀     ███    █▀      ██████████       ▀███▀███▀  █▀    ▀█   █▀     ▄████▀     ██████████   ███    ███        ███    ███  ▀██████▀    ███    █▀  ████████▀  
                                                                                                   ███    ███        ███    ███                                    
"""
print(titleCard)
time.sleep(2)

resource_types=["food","ammo","fuel"]
player_stats={
    "max_food":400,
    "current_food":400,
    "max_ammo":400,
    "current_ammo":400,
    "max_fuel":400,
    "current_fuel":400,
    "group":50,
    "trust":100,
    "morale":100,
    "rep":5
    } #these are the players current stats, all of these can change within their range

def merchant_encounter (player_stats,resource_types):
    print("* A lone merchant shuffles down the road towards you... *")
    time.sleep(2)
    choice=int(input("* Approach the Merchant? *\n 1.Lets see what he has for us          2.Not today\n"))
    match choice:
        case 1:
            print("* As your group rests for a bit you approach the merchant *")
            time.sleep(2)
            print("The Merchant: Greetings...")
            if player_stats["rep"]==0:
                print("The Merchant: The Road knows who you are. Disappear from my sight.")
            else:
        case 2:
            print("* The merchant shuffles away, murmuring to himself*")
            time.sleep(2)
            print("The Merchant: man these guys are broke...")
def bandit_encounter (player_stats,resource_types):
    bandits=random.randint(1,10)
    print("*",bandits,"low level bandits approach you, guns in hand *")
    time.sleep(2)
    print("The Bandits: HEY! THERES A FEE TO PASS!")
    time.sleep(2)
    choice=int(input("What do you do?\n 1. Pay the Fee          2. Try to reason with them          3. Last Resort, violence\n"))
    match choice:
        case 1:
            resource_fee=[random.choice(resource_types)]
            time.sleep(2)
            print("The Bandit: We're chargin ya some of your",resource_fee)
            time.sleep(2)
            print("The Bandit: Lets say...", random.randint(10,50),"of your",resource_fee)
        case 2:
            if player_stats["rep"]==10:
                print("The Bandits: Oh... you're The Leader.")
                time.sleep(2)
                print("The Bandits: Sorry for bothering ya... go ahead")
            else:
                print("The Bandits: Who do you think you are. Pay up, now.")
        case 3:
            print("*You command your group to open fire on the bandits*")
            coinflip=random.randint(1,2)
            if coinflip==1:
                time.sleep(2)
                print("* Luck is not on your side... You take casualties *")
                time.sleep(2)
                print("* As you walk away, you leave the corpse of 4 of your members... *")
                player_stats["group"] -= 4
                time.sleep(2)
                print("*",player_stats["group"],"members left *")
                time.sleep(2)
            else:
                time.sleep(2)
                print("Luck seems to be on your side, you suffer no casualties")
                time.sleep(2)
                print("-10 ammo")
                time.sleep(2)
                player_stats["current_ammo"] -= 10
                print(player_stats["current_ammo"],"left")

merchant_encounter (player_stats,resource_types)
