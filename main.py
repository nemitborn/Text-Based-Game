import time
import random
import encounters

titleCard = """
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

player_stats = encounters.player_stats
encounter_pool = [
    encounters.bandit_encounter,
    encounters.storm,
    encounters.creature,
    encounters.blockade,
    encounters.supply,
    encounters.speech,
    encounters.sing,
    encounters.cart,
    encounters.merchant_encounter
]

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
    time.sleep(1)
    print("Every day there will be 3 encounters you have to face. You will be presented with different options that correspond to a number")
    time.sleep(1)
    print("Use the number keys (1-9) to choose which action you would like to do")
    time.sleep(1)
    print("Use the ENTER key to confirm your choice and the Backspace key to delete whatever number you typed")
    time.sleep(1)
    print("Some encounters will require you to choose the correct side on a coinflip")
    time.sleep(1)
    print("Get it wrong and your group faces consequences, get it right and you'll get a favourable outcome")
    time.sleep(1)
def day_end(player_stats, day):
    # show stats and current day
    encounters.clear_screen()
    print("========== END OF DAY " + str(day) + " of 20 ==========")
    for stat, value in player_stats.items():
        print(stat.capitalize() + ": " + str(value))

    while True:
        choice = input("\nDo you want to continue? (y/n)\n").lower()
        if choice.startswith("y"):
            return True
        if choice.startswith("n"):
            return False
        print("Invalid input, Y or N dude")
def main_loop():
    for day in range(0, 20): #20 total days
        encounters.clear_screen()
        print("========== DAY " + str(day) + " of 20 ==========")
        time.sleep(1)

        for i in range(3): #3 encounters a day
            print("\n--- Day " + str(day) + ", Encounter " + str(i + 1) + "/3 ---\n")
            encounter = random.choice(encounter_pool)
            encounter(player_stats)
            encounters.gameover(player_stats)
            time.sleep(1)
            input("\nPress ENTER to continue...")
    #END OF GAME (after 20 days has passed)
    encounters.clear_screen()
    print("* After 20 long days, your group finally reaches the end of The Road... *")
    time.sleep(1)
    print("* " + str(player_stats["members"]) + " member(s) survived the journey *")

age_check()

encounters.clear_screen()
print(titleCard)
time.sleep(1)
choice = input("Welcome to WINTER ROAD, would you like a tutorial to begin?\n").lower()
time.sleep(1)
if choice.startswith("y"):
    tutorial()
    while True:
        choice = input("You got all that? or do you need me to repeat it again\n").lower()
        if choice.startswith("n"):
            print("listen up well this time...")
            time.sleep(1)
            tutorial()
        else:
            break
else:
    print("pshh okay you lil expert")
    time.sleep(1)

main_loop()
