import time
import os

import ascii_art
import inventory
player_stats=inventory.player_stats
def clear_screen():
    #clears the screen
    os.system("cls" if os.name == "nt" else "clear")

def say(text):      #This function was to simplify the printing process, this prevents me from repeating time.sleep after every print
    print(text)
    time.sleep(1)

def arrival(player_stats):  # the scene every player sees, no matter which ending they get, also determines which ending the player gets
    clear_screen()
    say("* On the tenth day, The Storm finally begins to die down... *")
    say("* The wind settles down, and for the first time since this started, the air does not sting...*")
    say("* Ahead, a wall of shipping containers stretches across the Road *")
    if player_stats["members"] == 1:
        say("* One survivor stands beside you. Just one. They carry the fighting spirit of the people before him... *")
    elif player_stats["members"] <= 4:
        say("* A small huddle of survivors stands behind you, too tired to speak *")
    else:
        say("* Behind you, a long line of survivors stretches back into the snow *")
    if player_stats["food"] < 50 and player_stats["ammo"] < 50 and player_stats["fuel"] < 50:
        say("* You've nothing left in your packs. You made it here on willpower alone... *")
    say("* Someone on the wall raises a rifle*")
    input("Press enter to continue...")
    #ENDING SELECTION
    if player_stats["trust"]>=8 and player_stats["morale"]>=8:
        HGL(player_stats)
    elif player_stats["rep"]>=7:
        SAINT(player_stats)
    elif player_stats["morale"]<=3:
        SG(player_stats)
    elif player_stats["rep"]<=3:
        INFAMY(player_stats)
    elif player_stats["trust"]<=3:
        RETRUBUTION(player_stats)
    else:
        NORMAL(player_stats)

#bad endings
def SG(player_stats): #only when morale<3
    clear_screen()
    say("* Your voice sounds like cracked soil in a drought *")
    say("You: Please... Shelter...")
    say("* The guard orders someone to open the gates *")
    say("* As the heavy metal doors swing open, your group shuffles inside... *")
    say("* No one utters a word to you, too much has been lost... *")
    say("* As you make your way in, you notice everyone's eyes are void of their fighting spirits... *")
    say("* You live with the consciousness that so many were lost just to get you to safety... *")
    say("* Why them and not you? *")
    say("========== ENDING: SURVIVOR'S GUILT ==========")
    input("Press enter to continue...")
    final_score(player_stats)

def INFAMY(player_stats):   #only possible when rep<3
    clear_screen()
    say("* Your raise your voice *")
    say("You: DON'T SHOOT! WE'RE FRIENDLY!")
    say("Guard: Tch, like we haven't heard that before. We know who you are.")
    say("* He orders for reinforcements... *")
    say("* As more rifles are raised against your group, you begin to realise...  *")
    say("* The Road remembers your sins... *")
    say("* You took advantage of people, but at what cost?... *")
    say("* Brutality is not the way. *")
    say("========== ENDING: INFAMY ==========")
    input("Press enter to continue...")
    final_score(player_stats)

def RETRUBUTION(player_stats):        #only possible when trust<3
    clear_screen()
    say("* Your raise your voice *")
    say("You: DON'T SHOOT! WE'RE FRIENDLY!")
    say("Guard: Tch, You sure? Your group dont seem to take a liking to you...")
    say("* He orders for someone to open the gate... *")
    say("* As you try to get through one of your members speak up...  *")
    say("Member: Please guard... our leader is horrible, they will cause chaos in this camp...")
    say("* As some guards block you off from entering you realise...*")
    say("* You should have been kinder to those who trusted you. *")
    say("========== ENDING: RETRIBUTION ==========")
    input("Press enter to continue...")
    final_score(player_stats)

#good endings
def HGL(player_stats):     #Only possible with both high morale and trust (more than or equal to 8)
    clear_screen()
    say("* Your voice sounds like a gong in an echo chamber...*")
    say("You: DON'T SHOOT! WE'RE FRIENDLY!")
    say("* The guard lowers down his rifle and studies you*")
    say("* He orders someone to open the gates for your group... *")
    say("* As the heavy metal doors swing open, your group lifts you up and carries you inside...  *")
    say("* As your group enters, everyone begins to chant your name... *")
    say("* You are a great leader. *")
    say("* Those who sacrificed everything were not left in vain. *")
    say("========== ENDING: HISTORY'S GREATEST LEADER ==========")
    input("Press enter to continue...")
    final_score(player_stats)

def SAINT(player_stats): #only when rep>7
    clear_screen()
    say("* Your voice booms across the sky... *")
    say("You: DON'T SHOOT! WE'RE FRIENDLY!")
    say("* The guard instantly lowers down his rifle, as if he recognises you... *")
    say("* He orders someone to open the gates for your group... *")
    say("*Guard: We have heard of you... The Road knows your name. Please, take shelter inside...  *")
    say("* As your group enters, everyone begins to chant your name... *")
    say("* You are a good person. *")
    say("* Those who sacrificed everything were not left in vain. *")
    say("========== ENDING: THE SAINT ==========")
    input("Press enter to continue...")
    final_score(player_stats)

def NORMAL(player_stats):        #if none of the conditions are met then this is the regular ending
    clear_screen()
    say("* Your voice raises to a shout*")
    say("You: DON'T SHOOT! WE'RE FRIENDLY!")
    say("* The guard lowers down his rifle and studies you*")
    say("* He orders someone to open the gates for your group... *")
    say("* As the heavy metal doors swing open, your group is taken into a solid concrete room... *")
    say("* As your group enters, each person is taken aside and questioned... *")
    say("* You served your purpose. *")
    say("* You could not have made it without your group. *")
    say("========== ENDING: NORMAL ==========")
    input("Press enter to continue...")
    final_score(player_stats)

# FINAL SCREEN
def final_score(player_stats):  # summary of the run, shown for every ending
    clear_screen()
    say("========== YOUR JOURNEY ==========")
    print("Survivors  :", player_stats["members"])
    print("Trust      :", player_stats["trust"])
    print("Morale     :", player_stats["morale"])
    print("Reputation :", player_stats["rep"], "  (the Road remembers...)")
    print("Food       :", player_stats["food"])
    print("Ammo       :", player_stats["ammo"])
    print("Fuel       :", player_stats["fuel"])
    print("==================================")
    time.sleep(3)
    print(ascii_art.Ending_quote)  # cool quote number 2
    time.sleep(2)
    say("\nIt doesn't have to end like this...")
    say("Maybe if your actions were different, your fate would change")
    time.sleep(5)
    exit()



