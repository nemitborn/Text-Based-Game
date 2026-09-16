import time
import random
def gameover(player_stats):
    if player_stats[""]
def coinFlip():
    coin=["heads","tails"]
    side=random.choice(coin)
    player_side=input("Choose a side. Heads or Tails?\n")
    player_side=player_side.lower()
    if player_side==side:
        return ("Pass")

    else:
        return ("Fail")
resource_types=["food","ammo","fuel"]
player_stats={
    "max_food":400,
    "current_food":400,
    "max_ammo":400,
    "current_ammo":400,
    "max_fuel":400,
    "current_fuel":400,
    "members":5,
    "trust":100,
    "morale":100,
    "rep":5
    }
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
            print("The Bandit: We're chargin ya some of your",resource_fee)
            time.sleep(2)
            fee={resource_fee: random.randint(10,50)}
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
            else:
                print("FAIL")
                print("The Bandits: Who do you think you are?")
                time.sleep(2)
                print("-10 ammo, -2 members")
                time.sleep(2)
                player_stats["current_ammo"] -= 10
                player_stats["members"] -= 2
                print("*",player_stats["members"],"members left... *")
        case 3:
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
bandit_encounter(player_stats,resource_types)
