import time
import random
player_stats={
    "current_food":400,
    "current_ammo":400,
    "current_fuel":400,
    "members":50,
    "trust":10,
    "morale":100,
    "rep":5
    }
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
resource_types=["food","ammo","fuel"]

def bandit_encounter (player_stats,resource_types):
    bandits=random.randint(1,10)
    print("*",bandits,"low level bandit(s) approach you, guns in hand *")
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
                if player_stats["current_ammo"]>=10:
                    player_stats["current_ammo"] -= 10
                    player_stats["members"] -= 2
                    gameover(player_stats)
                    print("-10 ammo, -2 members")
                    time.sleep(2)
                    print("*",player_stats["members"],"members left... *")
                else:
                    print("-10 members")
        case 3:
            if player_stats["current_ammo"]>=20:
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
bandit_encounter(player_stats,resource_types)
