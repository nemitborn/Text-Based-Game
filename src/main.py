import time
import random
import ascii_art
import encounters
import ending

player_stats = encounters.player_stats      #as the dictionary containing all the player's stats is repeated and printed a lot, I have put them in a variable to simplify development
encounter_pool = [      #a list of all the encounters that the player could face, does not include processes in encounter.py
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


#INTRO
age_check() #firstly checks the age

encounters.clear_screen()   #clears the screen
print(ascii_art.titleCard)    #wow, cool title card
time.sleep(5)
encounters.clear_screen()   #clears the title card
choice = input("Welcome to WINTER ROAD, would you like a tutorial to begin?\n>> ").lower()
time.sleep(1)
if choice.startswith("y") or choice.endswith("es"):
    tutorial()
    while True:     #constantly repeats the tutorial until the player says yes
        choice = input("You got all that?\n>> ").lower()
        if choice.startswith("n"):
            print("listen up well this time...")
            time.sleep(1)
            tutorial()
        else:
            break
else:
    print("\npshh okay you lil expert") #funny
    time.sleep(2)

for day in range(0, 1): #10 total days
    encounters.clear_screen()
    print(      #prints out the stats the player currently has
        "FOOD:",player_stats["food"],
        "\nAMMO:",player_stats["ammo"],
        "\nFUEL:",player_stats["fuel"],
        "\nTRUST:",player_stats["trust"],
        "\nMORALE:",player_stats["morale"]      #Members not included as the member count will be printed is some other encounters
    )       #Reputation is not included as it's meant to be hidden
    print("========== DAY " + str(day) + " of 10 ==========")       #Displays the current day
    input("Press ENTER to continue...")

    for i in range(0,3): #3 encounters a day
        print("\n--- Day " + str(day) + ", Encounter " + str(i + 1) + "/3 ---\n")
        encounter = random.choice(encounter_pool)   #selects a random encounter from the encounter pool and stores it
        encounter(player_stats) #calls the encounter and puts the player's stats in the parameters
        encounters.gameover(player_stats)  #actively checks if the player has less than 0 members after every encounter
        time.sleep(1)
        input("\nPress ENTER to continue...")
    encounters.clear_screen()   #clears the screen after every day has passed to prevent screen clutter
#END OF GAME (after 10 days has passed)
encounters.clear_screen()
ending.arrival(player_stats)
exit()
