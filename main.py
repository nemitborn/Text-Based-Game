import time
import encounters
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
player_stats=encounters.player_stats
resource_types=encounters.resource_types
encounter_pool = [
    encounters.bandit_encounter,
    encounters.storm,
    encounters.creature,
    encounters.blockade,
    encounters.supply,
    encounters.speech,
    encounters.sing,
    encounters.cart
] #a list of all the encounters
def age_check():
    try:
        age=int(input("Enter your age...\n"))
        if age>=16:
            print("WARNING - This game contains loud sounds, mentions of gun violence and death.")
            print(titleCard)
            time.sleep(2)
            input("Press 'ENTER' to continue...")
        else:
            print("You're not allowed to play this game. (16+ ONLY)")
            time.sleep(2)
            print("Age Check: FAILED")
            time.sleep(5)
            exit()
    except ValueError:
        print("Not a number.")
        time.sleep(2)
        print("Age Check: FAILED")
        time.sleep(5)
        exit()
def tutorial():
    print("WINTER ROAD is a text based game where you will need to guide your group and manage your resources whilst traveling across The Road")
    time.sleep(2)
    print("Every day there will be 3 encounters you have to face. You will be presented with different options that correspond to a number")
    time.sleep(2)
    print("Use the number keys (1-9) to choose which action you would like to do")
    time.sleep(2)
    print("Use the ENTER key to confirm your choice and the Backspace key to delete whatever number you typed")
    time.sleep(2)
    print("Some encounters will require you to choose the correct side on a coinflip")
    time.sleep(2)
    print("Get it wrong and your group faces consequences, get it right and you'll get a favourable outcome")
    time.sleep(2)
age_check()


#START MESSAGE
choice=input("Welcome to WINTER ROAD, would you like a tutorial to begin? (y/n)\n")
time.sleep(1)
if choice.startswith("y") or choice.endswith("es"):
    tutorial()
else:
    print("pshh okay you lil expert")
time.sleep(2)


#MAIN GAME LOOP
for day in range(0, 20): #20 days
    print("DAY",day,"/ 20")
    time.sleep(2)
    for i in range(0,3): #3 encounters per day
        encounter=random.choice(encounter_pool) #selects a random encounter
        encounter(player_stats) #calls it
        time.sleep(2)
    print("DAY", day, "COMPLETE")
    time.sleep(2)
    print("* You remind yourself that you need to rest and feed your group... *")
    player_stats["food"]-=player_stats["members"] #food is fed to your group proportional to the number of members
    player_stats["fuel"]-=20    #cost of staying warm
    time.sleep(2)
    print("-",player_stats["members"],"food         - 20 fuel")
    time.sleep(2)
    print(player_stats)
    input("Press 'ENTER' to continue...")
    time.sleep(2)
    if day==20:
        print("* You reach the safe zone... *")
