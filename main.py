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

def age_check():        #Checks to see if the player is 16+
    encounters.clear_screen()
    print("FULL SCREEN FOR THIS GAME TO WORK")      #needed for the ASCII art to display correctly
    time.sleep(2)
    input("\npress ENTER to continue...")
    try:
        age=int(input("\nEnter your age...\n>> "))
        if age>=16:
            print("WARNING - This game contains loud sounds, mentions of gun violence and death.")
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
    input()
    print("Every day there will be 3 encounters you have to face. You will be presented with different options that correspond to a number")
    input()
    print("Use the number keys (1-9) to choose which action you would like to do")
    input()
    print("Use the ENTER key to confirm your choice and the Backspace key to delete whatever number you typed")
    input()
    print("Some encounters will require you to choose the correct side on a coinflip")
    input()
    print("The coin flip only works with specific spelling, typing 'head' when you want to choose heads will cause you to fail the coin flip")
    input()
    print("Failing the coin flip will cause your group faces consequences, passing it means you'll get a favourable outcome")
    input()
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
        print(
            "FOOD:",player_stats["food"],
            "\nAMMO:",player_stats["ammo"],
            "\nFUEL:",player_stats["fuel"],
            "\nTRUST:",player_stats["trust"],
            "\nMORALE:",player_stats["morale"]
        )
        print("========== DAY " + str(day) + " of 20 ==========")       #Displays the current day
        input("Press ENTER to continue...")

        for i in range(0,3): #3 encounters a day
            print("\n--- Day " + str(day) + ", Encounter " + str(i + 1) + "/3 ---\n")
            encounter = random.choice(encounter_pool)
            encounter(player_stats)
            encounters.gameover(player_stats)  #actively checks if the player has less than 0 members after every encounter
            time.sleep(1)
            input("\nPress ENTER to continue...")
    #END OF GAME (after 20 days has passed)
    encounters.clear_screen()
    print("* 20 days have passed wowowowowo you won... *") #ADD THE ENDING
    time.sleep(1)
    print("* " + str(player_stats["members"]) + " member(s) survived the journey *")    #Displays the remaining members left in your group
    time.sleep(2)
    input("press ENTER to exit...")
    exit()

#INTRO
age_check() #firstly checks the age

encounters.clear_screen()   #clears the screen
print(titleCard)    #wow, cool title card
time.sleep(5)
encounters.clear_screen()   #clears the title card
choice = input("Welcome to WINTER ROAD, would you like a tutorial to begin?\n>>").lower()
time.sleep(1)
if choice.startswith("y") or choice.endswith("es"):
    tutorial()
    while True:     #constantly repeats the tutorial until the player says yes
        choice = input("You got all that?\n>>").lower()
        if choice.startswith("n"):
            print("listen up well this time...")
            time.sleep(1)
            tutorial()
        else:
            break
else:
    print("\npshh okay you lil expert") #funny
    time.sleep(2)

main_loop()
