import time
import random
from playsound3 import playsound
import processes
import inventory

current_stats=inventory.player_stats()
resource_types=["food","ammo","fuel"]   #contains the three different types of resources the player can gain or loose randomly

#NEGATIVE ENCOUNTERS
def bandit_encounter (current_stats):
    bandits=random.randint(1,10)
    print("*",bandits,"low level bandits approach you, guns in hand *")
    time.sleep(1)
    print("The Bandits: HEY! THERES A FEE TO PASS!")
    time.sleep(1)
    while True:
        try:
            choice=int(input("What do you do?\n 1. Pay the Fee          2. Try to reason with them          3. Last Resort, violence\n>> "))
            if choice==1 or choice==2 or choice==3:
                break
            else:
                print("* Please pick a number between 1 and 3. *")
        except ValueError:
            print("* That is not a number, try again. *")
    match choice:
        case 1:        #Pay the fee
            resource_fee = random.choice(resource_types)
            fee_price = random.randint(10, 50)
            print("The Bandit: We're chargin' ya some of your",resource_fee)
            time.sleep(1)
            print("The Bandit: Let's say...",fee_price,resource_fee)
            current_stats[resource_fee] = max(0,current_stats[resource_fee]-fee_price)    #Prevents the resource from going below 0
            time.sleep(1)
            print("-",fee_price,resource_fee)
            time.sleep(1)
            print("* At least you made it out alive... *")
        case 2:        #Reason
            if processes.coinFlip()=="Pass":
                if bandits<current_stats["members"]: #if the player has more members than there are bandits
                    print("PASS")
                    time.sleep(1)
                    print("* The Bandits hear you out and realise they're outnumbered *")
                else:   #if the player has fewer members than there are bandits
                    print("PASS")
                    time.sleep(1)
                    print("The Bandits: Man you're good at reasoning...")
                time.sleep(1)
                print("The Bandits: I guess we can make an exception for you... go on through")
            else:
                print("FAIL")
                time.sleep(1)
                print("The Bandits: Who do you think you are?")
                time.sleep(1)
                playsound("../sounds/gun2.mp3")     #gun fight ensues if the player fils the coin flip
                if current_stats["ammo"]>=10:    #if the player has 10 or more ammo
                    current_stats["ammo"] -= 10
                    current_stats["members"] -= 2
                    processes.gameover(current_stats)
                    print("-10 ammo, -2 members")
                    time.sleep(1)
                    print("*",current_stats["members"],"members left... *")
                else:   #if the player has less than 10 ammo they cannot fight back
                    print("-10 members")
                    current_stats["members"]-=10
                    processes.gameover(current_stats)
        case 3:         #Fight
            if current_stats["ammo"]>=20:    #if the player has more than 20 ammo
                playsound("../sounds/gun1.mp3")
                print("*You command your group to open fire on the bandits*")
                if processes.coinFlip()=="Pass":
                    print("PASS")
                    time.sleep(1)
                    print("* You take no casualties, it seems these were just lowly bandits *")
                    time.sleep(1)
                    current_stats["ammo"]-=20
                else:
                    print("FAIL")
                    time.sleep(1)
                    print("* You take casualties, 4 of your members are lost to these lowly bandits... *")
                    time.sleep(1)
                    print("-20 ammo         -4 members")
                    current_stats["ammo"]-=20
                    current_stats["members"]-=4
                    time.sleep(1)
                    print("*",current_stats["members"],"member(s) left... *")
            else:       #if the player has less than 20 ammo
                print("* You command your group to charge at the bandits... *")
                time.sleep(1)
                print("* You begin to remember an old saying from before all of this *")
                time.sleep(1)
                print("* Dont bring fists to a gun fight *")
                current_stats["members"] -= 10
                processes.gameover(current_stats)
                time.sleep(1)
                print("* You lose 10 of your members. You can feel their distrust in you... *")
                current_stats["trust"] -= 2
                time.sleep(1)
                print("*",current_stats["members"],"member(s) left... *")
def storm(current_stats):
    print("* As your group marches you feel a storm starting to pick up *")
    time.sleep(1)#ADD STORM SFX
    while True:
        try:
            choice = int(input("* What do you do?\n 1.Command your group to push through the storm          2.Maybe we should rest and wait for the storm to subside...\n>> "))
            if choice == 1 or choice == 2 or choice == 3:
                break
            else:
                print("* Please pick a number between 1 and 3. *")
        except ValueError:
            print("* That is not a number, try again. *")
    match choice:
        case 1:
            if current_stats["trust"] >= 5:
                # Make sure they have food first, then check the coin flip
                if current_stats["food"] >= 10 and processes.coinFlip() == "Pass":
                    print("PASS")
                    time.sleep(1)
                    print("* It took a while and a little bit of extra food, but your group managed to push through... *")
                    current_stats["food"] -= 10
                else:
                    print("FAIL")
                    time.sleep(1)
                    current_stats["members"] -= 5
                    print(f"* {current_stats['members']} members left... *")
                    time.sleep(1)
                    current_stats["trust"] = max(0, current_stats["trust"] - 1)
                    print("-1 trust")
                    time.sleep(1)
                    print("* You can start to hear the angry whispers of the group behind you... *")
                    processes.gameover(current_stats)
            else:
                print("* The group starts to murmur... they do not trust your leadership in this. *")
                time.sleep(1)
                print("* They decide it would be better to just rest and wait for the storm *")
                time.sleep(1)
                if current_stats["fuel"] >= 40:
                    print("* You end up using a bit more fuel than needed to survive that storm... *")
                    current_stats["fuel"]-=40
                else:
                    print("* As you rest you realise you don't have much fuel left, some of your members freeze in this storm... *")
                    time.sleep(1)
                    current_stats["members"]-=10
                    current_stats["morale"]=max(0, current_stats["morale"] - 1)
                    print("* The storm ends and you leave some of your group behind... *")
                    time.sleep(1)
                    print("*",current_stats['members'],"member(s) left... *")
                    time.sleep(1)
                    print("* You can feel the group losing their fighting spirit... *")
                    processes.gameover(current_stats)
        case 2:
            print("* The group seems to agree with your choice... *")
            time.sleep(1)
            if current_stats["fuel"]>=40:
                print("* You end up using a bit more fuel than needed to survive that storm... *")
                #FIRE SFX
                current_stats["fuel"]-=40
                time.sleep(1)
                print("* The group is fully rested and able to march on for a good while now... *")
                time.sleep(1)
                current_stats["trust"] += 1
                current_stats["morale"] += 1
                print("+1 trust         +1 morale")
            else:
                print("* As you rest you realise you dont have much fuel left, some of your members are sure to freeze in this storm... *")
                time.sleep(1) #STORM SFX
                current_stats["members"]-=10
                processes.gameover(current_stats)
                current_stats["morale"]-=1
                print("* The storm ends and you leave a some of your group behind... *")
                print("*", current_stats["members"], "member(s) left... *")
                time.sleep(1)
                print("* You can feel the group are losing their fighting spirit... *")
def creature(current_stats):
    print("* As your group takes a short rest, one of them hears the low snarl of something in the trees... *")
    #playsound("sounds/creature.mp3")
    while True:
        try:
            choice = int(input("What do you do?\n 1. Feed the beast          2. Try to run          3. Last Resort, violence\n>> "))
            if choice == 1 or choice == 2 or choice == 3:
                break
            else:
                print("* Please pick a number between 1 and 3. *")
        except ValueError:
            print("* That is not a number, try again. *")
    match choice:
        case 1:
            time.sleep(1)
            if current_stats["food"]>=10:
                current_stats["food"]-=10
                print("* You throw some food at the beast... *")
                time.sleep(1)
                print("* It seems to take it and retreats back to the trees... *")
            else:
                print("* You command the group to feed it, however you dont have anything to feed it... *")
                time.sleep(1)
                print("* You decided to just sacrifice some dude *")
                current_stats["members"]-=1
                processes.gameover(current_stats)
                print("*", current_stats["members"], "members left... *")
                time.sleep(1)
                current_stats["morale"]-=2
                current_stats["trust"]-=2
                print("* The rest of your group sees your actions and fear for their own lives... *")
        case 2:
            time.sleep(1)
            if processes.coinFlip()=="Pass":
                print("*  Your group outruns the beast, seems like it was injured... *")
            else:
                print("* Most of your group outruns the beast, however there are some that got left behind and eaten... *")
                current_stats["members"]-=5
                processes.gameover(current_stats)
                time.sleep(1)
                print("*", current_stats["members"], "members left... *")
                current_stats["morale"]-=1
                time.sleep(1)
                print("* The group seems to lose their fighting spirit even more... *")
        case 3:
            time.sleep(1)
            if current_stats["ammo"]>=10:
                if processes.coinFlip()=="Pass":
                    print("PASS")
                    playsound("../sounds/gun1.mp3")
                    print("* You command your group to shoot at the beast... *")
                    time.sleep(1)
                    print("* it seems to run away in fear back into the trees... *")
                    current_stats["ammo"]-=10
                else:
                    print("FAIL")
                    playsound("../sounds/gun1.mp3")
                    print("* You command your group to shoot at the beast... *")
                    playsound("../sounds/gun2.mp3")
                    print("* As you shoot the beast you see it pouncing on your members... *")
                    current_stats["members"]-=3
                    processes.gameover(current_stats)
                    print("*", current_stats["members"], "members left... *")
                    current_stats["morale"]-=1
                    print("* The group seems to lose their fighting spirit even more... *")
            else:
                print("* You reach for your weapons, but you're out of ammo... *")
                time.sleep(1)
                current_stats["members"]-=3
                processes.gameover(current_stats)
                print("* The beast gets to a few of your group before fleeing... *")
                print("*", current_stats["members"], "members left... *")

#NEUTRAL ENCOUNTERS
def blockade(current_stats):
    print("* As your group marches through the snow, you come across a blockade... *")
    time.sleep(1)
    print("* It seems to be a bunch of cars and rubble, stacked upon each other... *")
    while True:
        try:
            choice = int(input("What do you do?\n 1. Go around          2. Maybe this is a sign to rest for a bit          3. Target Practice (REQS AMMO)\n>> "))
            if choice == 1 or choice == 2 or choice == 3:
                break
            else:
                print("* Please pick a number between 1 and 3. *")
        except ValueError:
            print("* That is not a number, try again. *")
    match choice:
        case 1:
            if processes.coinFlip()=="Pass":
                print("PASS")
                time.sleep(1)
                print("* Even though your group was convinced it was an ambush, turns out you're safe... *")
                time.sleep(1)
                print("* The group seems to trust you a little more now *")
                current_stats["trust"]+=1
            else:
                print("* A group of bandits were waiting to ambush your group *")
                if current_stats["ammo"]>=30:
                    time.sleep(1)
                    print("* Your group raises their guns and begins to fire *")
                    playsound("../sounds/gun1.mp3")
                    if processes.coinFlip()=="Pass":
                        print("PASS")
                        time.sleep(1)
                        print("* Your group effortlessly takes the bandits down and defends themselves... *")
                        current_stats["ammo"]-=30
                        time.sleep(1)
                        print("-30 ammo")
                    else:
                        print("FAIL")
                        time.sleep(1)
                        print("* Your group fights their hardest but they still take casualties... *")
                        current_stats["members"]-=5
                        processes.gameover(current_stats)
                        current_stats["ammo"]-=30
                        time.sleep(1)
                        print("-30 ammo")
                        print("*",current_stats["members"],"member(s) left... *")
                else:
                    # No ammo to fight back with
                    print("* You have no ammo to fight back with... *")
                    time.sleep(1)
                    current_stats["members"]-=8
                    processes.gameover(current_stats)
                    print("* The bandits overwhelm your group... *")
                    print("*",current_stats["members"],"member(s) left... *")
        case 2:
            if current_stats["fuel"]>=10:
                print("* Your group decides to take a well needed rest... *")
                time.sleep(1)
                print("* They start a big fire to heat themselves up *")
                time.sleep(1)
                print("-10 fuel")
                current_stats["fuel"]-=10
                current_stats["morale"]+=1
            else:
                print("* Your group decides to rest, however there's no fuel to burn *")
                current_stats["members"]-=1
                processes.gameover(current_stats)
                time.sleep(1)
                print("* It seems one of the weaker members has fallen to frostbite *")
                time.sleep(1)
        case 3:
            if current_stats["ammo"]>=50:
                print("* One of your group members grabs their gun and shoots the cars out of rage... *")
                playsound("../sounds/gun2.mp3")
                print("* Others begin to join in... *")
                playsound("../sounds/gun1.mp3")
                if processes.coinFlip()=="Pass":
                    print("PASS")
                    time.sleep(1)
                    print("* One of the bullets strikes the fuel tank of the cars... *")
                    time.sleep(1)
                    print("* A subtle spark turns the entire barricade into a fireball... *")
                    time.sleep(1)
                    print("* As your group cheers at the wreckage they caused, you can feel their fighting spirits ignite once more *")
                    print("* -40 ammo *")
                    current_stats["ammo"]-=40
                    current_stats["morale"]+=1
                else:
                    print("* As the gun fire dies down, the first shooter realises hes been shooting an empty gun for a while now... *")
                    time.sleep(1)
                    print("* You manage to calm them down and decide to just walk around the blockade... *")
                    current_stats["ammo"]-=30
                    current_stats["morale"]-=1
                    print("* The group's fighting sprit seems to die down just a little bit... *")
            else:
                print("* You don't have enough ammo for that... *")
                time.sleep(1)
                print("* You decide to just walk around instead... *")
def merchant_encounter(current_stats):
    print("* In the distance you spot a lone figure with a heavily laden sled... *")
    time.sleep(1)
    approach = input("Do you want to approach the merchant? (y/n)\n>> ").lower()
    if not approach.startswith("y"):
        print("* You decide to keep your distance and move on... *")
        return
    time.sleep(1)
    if current_stats["rep"] < 4:
        print("The Merchant: The Road knows who you are. Get lost...")
        return
    print("The Merchant: Aha, welcome.... Looking to trade?")
    time.sleep(1)
    while True:
        try:
            choice = int(input("What do you do?\n 1. Open shop          2. Steal from the merchant          3. Quit\n>> "))
            if choice == 1 or choice == 2 or choice == 3:
                break
            else:
                print("* Please pick a number between 1 and 3. *")
        except ValueError:
            print("* That is not a number, try again. *")
    match choice:
        case "1":
            processes.merchant_shop(current_stats)
        case "2":
            print("* Whilst you are bargaining with the merchant, one of your members sneaks around and grabs some of his loot*")
            time.sleep(1)
            if processes.coinFlip() == "Pass":
                print("PASS")
                processes.random_loot(current_stats)
            else:
                print("FAIL")
                time.sleep(1)
                print("* The merchant catches them red-handed *")
                time.sleep(1)
                print("The Merchant: HEY! PUT THAT BACK!")
                current_stats["ammo"] -= 1
                playsound("../sounds/gun2.mp3")
                current_stats["rep"] -= 2
                time.sleep(1)
                print("-1 ammo")
                time.sleep(1)
                print("* You feel as if you've commited a great sin, how can anyone look at you the same... *")
        case "3":
            print("* You decide against it and walk away... *")
def butcher_encounter(current_stats):
    print("* In the distance you see a small wooden hut *")
    approach = input("Do you want to approach the hut? (y/n)\n>> ").lower()
    if not approach.startswith("y"):
        print("* You decide to keep your distance and move on... *")
        return      #ends the function and returns nothing
    time.sleep(1)
    print("The Butcher: What do you want... You lookin to trade?")
    time.sleep(1)
    while True:
        try:
            choice=int(input("What do you do?\n 1. Open shop          2. Steal from the butcher          3. Quit\n>> "))
            if choice==1 or choice==2 or choice==3:
                break
            else:
                print("* Please pick a number between 1 and 3. *")
        except ValueError:
            print("* That is not a number, try again. *")
    match choice:
        case 1:
            processes.butcher_shop(current_stats)
        case 2:
            print("* Whilst you are talking to the butcher, one of your members sneaks around and grabs some of his loot*")
            time.sleep(1)
            if processes.coinFlip() == "Pass":
                print("PASS")
                time.sleep(1)
                processes.random_loot(current_stats)
            else:
                print("FAIL")
                time.sleep(1)
                print("* The butcher catches you and hurls a cleaver at their head... *")
                time.sleep(1)
                print("The Butcher: GET OUT NOW!")
                current_stats["rep"]-=1
                time.sleep(1)
                print("* You feel as if everyone saw what you attempted to do... *")
        case 3:
            print("* You decide against it and walk away... *")

#POSITIVE ENCOUNTERS
def supply(current_stats):
    print("* As you stumble through the snow, you come across a large crate with a parachute attached... *")
    time.sleep(1)
    print("* As your group surrounds it it's clear there's a few supplies around the crash site... *")
    time.sleep(1)
    print("* The large crate seems to pry open, however it's not clear if you can... *")
    if processes.coinFlip()=="Pass":
        print("PASS")
        time.sleep(1)
        print("* Through all your efforts, the crate finally lifts open... *")
        processes.random_loot(current_stats)
    else:
        print("FAIL")
        time.sleep(1)
        print("* Despite all your effort, the crate will not open... *")
        time.sleep(1)
        print("* You find comfort in the fact you still got something for free in this world... *")
        time.sleep(1)
    print("+ 20 ammo")
    current_stats["ammo"]+=20
def speech(current_stats):
    print("* As your group marches through the snow, you can tell their morale is low... *")
    time.sleep(1)
    print("* You turn around and raise your hand to halt them. *")
    time.sleep(1)
    print("* The wind blows from behind you as you stand in front of all your group *")
    time.sleep(1)
    print("* You open your mouth to say something... *")
    while True:
        try:
            choice = int(input("What do you say?\n1. Encourage spirits\n2. Strengthen bond\n3. Remind them what they fight for\n>> "))
            if choice==1 or choice==2 or choice==3:
                break
            else:
                print("* Please pick a number between 1 and 3. *")
        except ValueError:
            print("* That is not a number, try again. *")
            time.sleep(1)
    match choice:
        case 1:
            print("* The speech riles your group up, you feel their fighting spirit ignite once more... *")
            time.sleep(1)
            print("+1 Morale")
            current_stats["morale"]+=1
        case 2:
            print("* The speech reaches the hearts of many of your members, you feel as if they are your real family now.. *")
            time.sleep(1)
            print("+1 Trust")
            current_stats["trust"]+=1
        case 3:
            if processes.coinFlip()=="Pass":
                print("PASS")
                time.sleep(1)
                print("The speech strikes the soul of your entire group. Their loyalty can be felt through the air")
                current_stats["trust"]+=1
                current_stats["morale"]+=1
                print("+1 Morale")
                time.sleep(1)
                print("+1 Trust")
            else:
                print("FAIL")
                time.sleep(1)
                print("* The wind continues to blow as none of your group speaks up... *")
                time.sleep(1)
                print("* It seems as if the speech hasn't resonated with anyone in the group... *")
                time.sleep(1)
                print("* As you lower your hand and turn around to continue to march, one small thought digs into your head... *")
                time.sleep(1)
                print("* 'Tough crowd huh...' *")
def sing(current_stats):
    print("* As your group marches, the wind begins to howl... *")
    time.sleep(1)
    print("* The sounds of the winds and the sounds of walking combine and sound eerily similar to a popular song before all of this... *")
    time.sleep(1)
    print("* To pass the time, one of your group members begins to sing that very song... *")
    time.sleep(1)
    print("* More and more people join in, and soon, everyone is singing... *")
    time.sleep(1)
    current_stats["morale"]+=1
    print("+1 morale")
def cart(current_stats):
    print("* As your group continues on their journey, you come a crashed wooden cart... *")
    time.sleep(1)
    print("* It seems as if the wheel has came off. Whoever drove it took whatever he could hold and ran off... *")
    time.sleep(1)
    print("* Maybe its best if we just take what they left behind, not like they're using it anyways... *")
    time.sleep(1)
    processes.random_loot(current_stats)
