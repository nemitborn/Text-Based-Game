import time
import os
import encounters

player_stats=encounters.player_stats
def clear_screen():
    #clears the screen
    os.system("cls" if os.name == "nt" else "clear")
def arrival(player_stats):  # the scene every player sees, no matter which ending they get
    clear_screen()
    print("* On the tenth day, The Storm finally begins to die down... *", )
    time.sleep(1)
    print("* The wind settles down, and for the first time since this started, the air does not sting...*", )
    time.sleep(1)
    print("* Ahead, a wall of shipping containers stretches across the Road *", )
    time.sleep(1)
    if player_stats["members"] == 1:
        print("* One survivor stands beside you. Just one. They carry the fighting spirit of the people before him... *", )
    elif player_stats["members"] <= 4:
        print("* A small huddle of survivors stands behind you, too tired to speak *", )
    else:
        print("* Behind you, a long line of survivors stretches back into the snow *", )
    if (player_stats["food"] < 50 and player_stats["ammo"] < 50
            and player_stats["fuel"] < 50):
        print("* You've nothing left in your packs. You made it here on willpower alone... *", )
    time.sleep(1)
    print("* Someone on the wall raises a rifle... then slowly lowers it *", )
    time.sleep(1)
    print("The Warden: STOP THERE. State your business.", )
    final_screen(player_stats)


def final_screen(player_stats):  # summary of the run, shown for every ending
    time.sleep(1)
    clear_screen()
    print("========== YOUR JOURNEY ==========")
    time.sleep(1)
    print("Survivors  :", player_stats["members"])
    print("Trust      :", player_stats["trust"])
    print("Morale     :", player_stats["morale"])
    print("Reputation :", player_stats["rep"], "  (the Road remembers...)")
    print("Food       :", player_stats["food"])
    print("Ammo       :", player_stats["ammo"])
    print("Fuel       :", player_stats["fuel"])
    print("==================================")
    time.sleep(3)
    print("\nMEMENTO VIVERE")  # mirrors the "MEMENTO MORI" on the game over screen
    time.sleep(2)
    print("\nYou live to die another day...")