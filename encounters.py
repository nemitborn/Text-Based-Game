import time
import random
from playsound3 import playsound
player_stats={
    "current_food":10,
    "current_ammo":100,
    "current_fuel":40,
    "members":1,
    "trust":1,
    "morale":10,
    "rep":5
    }
resource_types=["food","ammo","fuel"]
def gameover(player_stats):
    if player_stats["members"]<=0:
        print("* The final member of your group has perished*")
        time.sleep(2)
        print("* You have led your team to their death... *")
        time.sleep(60)
        exit()
def coinFlip():
    coin=["heads","tails"]
    side=random.choice(coin)
    player_side=input("Choose a side. Heads or Tails?\n")
    player_side=player_side.lower()
    if player_side==side:
        return "Pass"

    else:
        return "Fail"
def bandit_encounter (player_stats,resource_types):
    bandits=random.randint(1,10)
    print("* some low level bandits approach you, guns in hand *")
    time.sleep(2)
    print("The Bandits: HEY! THERES A FEE TO PASS!")
    time.sleep(2)
    choice=int(input("What do you do?\n 1. Pay the Fee          2. Try to reason with them          3. Last Resort, violence\n"))
    match choice:
        case 1:
            resource_fee=[random.choice(resource_types)]
            print("The Bandit: We're chargin ya some of your",resource_fee)
            time.sleep(2)
            fee=[random.randint(10,50),resource_fee]
            print("The Bandit: Lets say...",fee)
            player_stats[resource_fee]-=resource_fee

        case 2:
            if coinFlip()=="Pass":
                if bandits<player_stats["members"]:
                    print("PASS")
                    print("* The Bandits hear you out and realise they're outnumbered *")
                else:
                    print("PASS")
                    time.sleep(2)
                    print("The Bandits: Man you're good at reasoning...")
                time.sleep(2)
                print("The Bandits: I guess we can make an exception for you... go on through")
            elif coinFlip()=="Fail":
                print("FAIL")
                time.sleep(2)
                print("The Bandits: Who do you think you are?")
                time.sleep(2)
                playsound("sounds/gun2.mp3")
                if player_stats["current_ammo"]>=10:
                    player_stats["current_ammo"] -= 10
                    player_stats["members"] -= 2
                    gameover(player_stats)
                    print("-10 ammo, -2 members")
                    time.sleep(2)
                    print("*",player_stats["members"],"members left... *")
                else:
                    print("-10 members")
                    gameover(player_stats)
        case 3:
            if player_stats["current_ammo"]>=20:
                playsound("sounds/gun1.mp3")
                print("*You command your group to open fire on the bandits*")
                if coinFlip()=="Pass":
                    print("PASS")
                    time.sleep(2)
                    print("* You take no casualties, it seems these were just lowly bandits *")
                else:
                    print("FAIL")
                    time.sleep(2)
                    print("* You take casualties, 4 of your members are lost to these lowly bandits... *")
                    time.sleep(2)
                    print("-20 ammo         -4 members")
                    player_stats["current_ammo"] -= 20
                    player_stats["members"] -= 4
                    time.sleep(2)
                    print("*",player_stats["members"],"member(s) left... *")
            else:
                print("* You command your group to charge at the bandits... *")
                time.sleep(2)
                print("* You begin to remember an old saying from before all of this *")
                time.sleep(2)
                print("* Dont bring fists to a gun fight *")
                player_stats["members"] -= 10
                gameover(player_stats)
                time.sleep(2)
                print("* You loose 10 of your members. You can feel their distrust in you... *")
                player_stats["trust"] -= 2
                time.sleep(2)
                print("*",player_stats["members"],"member(s) left... *")
def storm(player_stats):
    print("* As your group marches you feel a storm starting to pick up *")
    time.sleep(2)
    choice=int(input("* What do you do?\n 1.Command your group to push through the storm          2.Maybe we should rest and wait for the storm to subside...\n"))
    match choice:
        case 1:
            if player_stats["trust"]>=5:
                if coinFlip()=="Pass" and player_stats["current_food"]>=10:
                    print("PASS")
                    time.sleep(2)
                    print("* It took a while and a little bit of extra food but your group managed to push through... *")
                else:
                    print("FAIL")
                    time.sleep(2)
                    player_stats["members"]-=5
                    gameover(player_stats)
                    print("*", player_stats["members"], "members left... *")
                    player_stats["morale"] -= 1
                    player_stats["trust"] -= 1
                    print("* You can start to hear the angry whispers of the group behind you... *")
            else:
                print("* The group starts to murmur... they do not trust your leadership in this. *")
                time.sleep(2)
                print("* They decide it would be better to just rest and wait for the storm *")
                time.sleep(2)
                if player_stats["current_fuel"] >= 40:
                    print("* You end up using a bit more fuel than needed to survive that storm... *")
                    player_stats["current_fuel"] -= 40
                else:
                    print("* As you rest you realise you dont have much fuel left, some of your members are sure to freeze in this storm... *")
                    time.sleep(2)
                    player_stats["members"] -= 10
                    gameover(player_stats)
                    player_stats["morale"] -= 1
                    print("* The storm ends and you leave a some of your group behind... *")
                    time.sleep(2)
                    print("*", player_stats["members"], "member(s) left... *")
                    time.sleep(2)
                    print("* You can feel the group are loosing their fighting spirit... *")
        case 2:
            print("* The group seems to agree with your choice... *")
            time.sleep(2)
            if player_stats["current_fuel"]>=40:
                print("* You end up using a bit more fuel than needed to survive that storm... *")
                player_stats["current_fuel"]-=40
            else:
                print("* As you rest you realise you dont have much fuel left, some of your members are sure to freeze in this storm... *")
                time.sleep(2)
                player_stats["members"]-=10
                gameover(player_stats)
                player_stats["morale"]-=1
                print("* The storm ends and you leave a some of your group behind... *")
                print("*", player_stats["members"], "member(s) left... *")
                time.sleep(2)
                print("* You can feel the group are loosing their fighting spirit... *")
def creature(player_stats):
    print("* As your group takes a short rest, one of them hears the low snarl of something in the trees... *")
    time.sleep(2)
    choice=int(input("What do you do?\n 1. Feed the beast          2. Try to run          3. Last Resort, violence\n"))
    match choice:
        case 1:
            time.sleep(2)
            if player_stats["curent_food"]>=10:
                player_stats["current_food"]-=10
                print("* You throw some food at the beast... *")
                time.sleep(2)
                print("* It seems to take it and retreats back to the trees... *")
            else:
                print("* You command the group to feed it, however you dont have anything to feed it... *")
                time.sleep(2)
                print("* You decided to just sacrifice some dude *")
                player_stats["members"]-=1
                gameover(player_stats)
                print("*", player_stats["members"], "members left... *")
                time.sleep(2)
                player_stats["morale"]-=2
                player_stats["trusts"]-=2
                print("* The rest of your group sees your actions and fear for their own lives... *")
        case 2:
            time.sleep(2)
            if coinFlip()=="Pass":
                print("*  Your group outruns the beast, seems like it was injured... *")
            else:
                print("* Most of your group outruns the beast, however there are some that got left behind and eaten... *")
                player_stats["members"]-=5
                gameover(player_stats)
                time.sleep(2)
                print("*", player_stats["members"], "members left... *")
                player_stats["morale"]-=1
                time.sleep(2)
                print("* The group seems to loose their fighting spirit even more... *")
        case 3:
            time.sleep(2)
            if player_stats["current_ammo"]>=10:
                if coinFlip()=="Pass":
                    print("PASS")
                    playsound("sound/gun1.mp3")
                    print("* You command your group to shoot at the beast... *")
                    time.sleep(2)
                    print("* it seems to run away in fear back into the trees... *")
                    player_stats["current_ammo"]-=10
                else:
                    print("FAIL")
                    playsound("sounds/gun1.mp3")
                    print("* You command your group to shoot at the beast... *")
                    playsound("sound/gun2.mp3")
                    print("* As you shoot the beast you see it pouncing on your members... *")
                    player_stats["members"]-=3
                    gameover(player_stats)
                    print("*", player_stats["members"], "members left... *")
                    player_stats["morale"]-=1
                    print("* The group seems to loose their fighting spirit even more... *")

creature(player_stats)
