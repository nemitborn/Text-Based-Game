import time
import random
import os
from playsound3 import playsound
import ascii_art

player_stats={
    "food":400,
    "ammo":400,
    "fuel":400,
    "members":1,
    "trust":6,
    "morale":5,
    "rep":5
    }   #Contains all the player information
resource_types=["food","ammo","fuel"]   #contains the three different types of resources the player can gain or loose randomly

#non encounters but still processes
def random_loot(player_stats):  #this function generates and adds random loot, used in a lot of encounters
    supply_loot = random.choice(resource_types) #chooses a random type of resource from resource_types
    supply_amount = random.randint(40, 80)     #chooses a random number in between 40 and 80 to give to the player
    time.sleep(1)
    print("* Inside you find", supply_amount, supply_loot, "*") #notifies the player that they found the loot
    player_stats[supply_loot] += supply_amount      #Adds it to their stats
    time.sleep(1)
    print("+", supply_amount, supply_loot)  #prints a message to notify the player
def clear_screen():
    #clears the screen
    os.system("cls" if os.name == "nt" else "clear")
def merchant_shop(player_stats):    #a seperate function for the merchant shop
    print("* The merchant lays out their goods... *")
    time.sleep(1)
    while True: #Always initiates the loop
        print("\n--- Merchant's Shop ---")
        for stat in resource_types:
            print(stat.capitalize(),": ",str(player_stats[stat]))
        print("\nTrade rate: 10 of one resource for 8 of another")      #Like an exchange rate with currencies
        choice = input("What would you like to do?\n 1. Make a trade          2. Leave the shop\n")
        if choice == "1":
            give = input("What do you want to give up? (food, ammo, fuel)\n").lower()   #what the player gives the merchant
            get = input("What do you want in return? (food, ammo, fuel)\n").lower()     #what the player gets from the merchant
            if give not in resource_types or get not in resource_types: #if either option is not in the listed items the player can receive or get
                print("* The Merchant: Aha.. Im afraid I dont have that in stock. But you're welcome to pick something else... *")
                continue    #loops back to the start
            if give == get:
                print("* The merchant laughs at you... *")
                time.sleep(1)
                print("*The Merchant: Aha, a jokester I see. Alright now, lets do some actual trading *")
                continue
            if player_stats[give] < 3:  #if the player does not have enough to trade
                print("* You don't have enough ",give," to make that trade... *")
                continue

            player_stats[give]-=10
            player_stats[get]+=8
            print("* You trade 10 ",give," for 8 ",get," *")
            time.sleep(1)
        else:
            print("* You thank the merchant and continue on your way... *")
            break
def gameover(player_stats):     #This is a function that checks if the player has less or equal to 0 members in their group
    if player_stats["members"]<=0:
        print("* The final member of your group has perished*")
        time.sleep(1)
        print("* You have led your team to their death... *")
        time.sleep(1)
        print(ascii_art.GameOver)
        time.sleep(5)
        print("MEMENTO MORI")       #cool quote
        time.sleep(2)
        exit()
def coinFlip():     #The coin flip used in many situations
    coin=["heads","tails"]      #two sides of the coin
    side=random.choice(coin)    #picks a random side
    player_side=input("Choose a side. Heads or Tails?\n>> ")
    player_side=player_side.lower() #
    if player_side==side:
        return "Pass"

    else:
        return "Fail"

#negative encounters
def bandit_encounter (player_stats):
    bandits=random.randint(1,10)
    print("* some low level bandits approach you, guns in hand *")
    time.sleep(1)
    print("The Bandits: HEY! THERES A FEE TO PASS!")
    time.sleep(1)
    choice=int(input("What do you do?\n 1. Pay the Fee          2. Try to reason with them          3. Last Resort, violence\n>> "))
    match choice:
        case 1:        #Pay the fee
            resource_fee=random.choice(resource_types)
            fee_price=random.randint(10, 50)
            print("The Bandit: We're chargin ya some of your",resource_fee)
            time.sleep(1)
            print("The Bandit: Lets say...",fee_price,resource_fee)
            player_stats[resource_fee]-=fee_price
            time.sleep(1)
            print("-",fee_price,resource_fee)
        case 2:        #Reason
            if coinFlip()=="Pass":
                if bandits<player_stats["members"]:
                    print("PASS")
                    time.sleep(1)
                    print("* The Bandits hear you out and realise they're outnumbered *")
                else:
                    print("PASS")
                    time.sleep(1)
                    print("The Bandits: Man you're good at reasoning...")
                time.sleep(1)
                print("The Bandits: I guess we can make an exception for you... go on through")
            elif coinFlip()=="Fail":
                print("FAIL")
                time.sleep(1)
                print("The Bandits: Who do you think you are?")
                time.sleep(1)
                playsound("../sounds/gun2.mp3")
                if player_stats["ammo"]>=10:
                    player_stats["ammo"] -= 10
                    player_stats["members"] -= 2
                    gameover(player_stats)
                    print("-10 ammo, -2 members")
                    time.sleep(1)
                    print("*",player_stats["members"],"members left... *")
                else:
                    print("-10 members")
                    gameover(player_stats)
        case 3:         #Fight
            if player_stats["ammo"]>=20:
                playsound("../sounds/gun1.mp3")
                print("*You command your group to open fire on the bandits*")
                if coinFlip()=="Pass":
                    print("PASS")
                    time.sleep(1)
                    print("* You take no casualties, it seems these were just lowly bandits *")
                else:
                    print("FAIL")
                    time.sleep(1)
                    print("* You take casualties, 4 of your members are lost to these lowly bandits... *")
                    time.sleep(1)
                    print("-20 ammo         -4 members")
                    player_stats["ammo"] -= 20
                    player_stats["members"] -= 4
                    time.sleep(1)
                    print("*",player_stats["members"],"member(s) left... *")
            else:
                print("* You command your group to charge at the bandits... *")
                time.sleep(1)
                print("* You begin to remember an old saying from before all of this *")
                time.sleep(1)
                print("* Dont bring fists to a gun fight *")
                player_stats["members"] -= 10
                gameover(player_stats)
                time.sleep(1)
                print("* You loose 10 of your members. You can feel their distrust in you... *")
                player_stats["trust"] -= 2
                time.sleep(1)
                print("*",player_stats["members"],"member(s) left... *")
def storm(player_stats):
    print("* As your group marches you feel a storm starting to pick up *")
    time.sleep(1)#ADD STORM SFX
    choice=int(input("* What do you do?\n 1.Command your group to push through the storm          2.Maybe we should rest and wait for the storm to subside...\n>> "))
    match choice:
        case 1:
            if player_stats["trust"]>=5:    #If trust is below 5, the group won't listen to the player
                if coinFlip()=="Pass" and player_stats["food"]>=10:     #checks if the player has enough food/energy for their group to make it through the storm
                    print("PASS")
                    time.sleep(1)
                    print("* It took a while and a little bit of extra food but your group managed to push through... *")
                    player_stats["food"]-=10
                else:
                    print("FAIL")
                    time.sleep(1)
                    player_stats["members"]-=5
                    gameover(player_stats)
                    print("*", player_stats["members"], "members left... *")
                    time.sleep(1)
                    player_stats["trust"] -= 1
                    print("-1 trust")
                    time.sleep(1)
                    print("* You can start to hear the angry whispers of the group behind you... *")
            else:
                print("* The group starts to murmur... they do not trust your leadership in this. *")
                time.sleep(1)
                print("* They decide it would be better to just rest and wait for the storm *")
                time.sleep(1)
                if player_stats["fuel"] >= 40:      #a lot of fuel used
                    #ADD FIRE SFX
                    print("* You end up using a bit more fuel than needed to survive that storm... *")
                    player_stats["fuel"] -= 40
                else:   #if the player has no fuel to rest in the storm, people die
                    print("* As you rest you realise you dont have much fuel left, some of your members are sure to freeze in this storm... *")
                    time.sleep(1)
                    player_stats["members"] -= 10
                    gameover(player_stats)
                    player_stats["morale"] -= 1
                    print("* The storm ends and you leave a some of your group behind... *")
                    #ADD STORM SFX
                    time.sleep(1)
                    print("*", player_stats["members"], "member(s) left... *")
                    time.sleep(1)
                    print("* You can feel the group are loosing their fighting spirit... *")
        case 2:
            print("* The group seems to agree with your choice... *")
            time.sleep(1)
            if player_stats["fuel"]>=40:
                print("* You end up using a bit more fuel than needed to survive that storm... *")
                #FIRE SFX
                player_stats["fuel"]-=40
                time.sleep(1)
                print("* The group is fully rested and able to march on for a good while now... *")
                time.sleep(1)
                player_stats["trust"] += 1
                player_stats["morale"] += 1
                print("+1 trust         +1 morale")
            else:
                print("* As you rest you realise you dont have much fuel left, some of your members are sure to freeze in this storm... *")
                time.sleep(1) #STORM SFX
                player_stats["members"]-=10
                gameover(player_stats)
                player_stats["morale"]-=1
                print("* The storm ends and you leave a some of your group behind... *")
                print("*", player_stats["members"], "member(s) left... *")
                time.sleep(1)
                print("* You can feel the group are loosing their fighting spirit... *")
def creature(player_stats):
    print("* As your group takes a short rest, one of them hears the low snarl of something in the trees... *")
    #playsound("sounds/creature.mp3")
    choice=int(input("What do you do?\n 1. Feed the beast          2. Try to run          3. Last Resort, violence\n>> "))
    match choice:
        case 1:
            time.sleep(1)
            if player_stats["food"]>=10:
                player_stats["food"]-=10
                print("* You throw some food at the beast... *")
                time.sleep(1)
                print("* It seems to take it and retreats back to the trees... *")
            else:
                print("* You command the group to feed it, however you dont have anything to feed it... *")
                time.sleep(1)
                print("* You decided to just sacrifice some dude *")
                player_stats["members"]-=1
                gameover(player_stats)
                print("*", player_stats["members"], "members left... *")
                time.sleep(1)
                player_stats["morale"]-=2
                player_stats["trust"]-=2  # was "trusts" - that key doesn't exist in player_stats
                print("* The rest of your group sees your actions and fear for their own lives... *")
        case 2:
            time.sleep(1)
            if coinFlip()=="Pass":
                print("*  Your group outruns the beast, seems like it was injured... *")
            else:
                print("* Most of your group outruns the beast, however there are some that got left behind and eaten... *")
                player_stats["members"]-=5
                gameover(player_stats)
                time.sleep(1)
                print("*", player_stats["members"], "members left... *")
                player_stats["morale"]-=1
                time.sleep(1)
                print("* The group seems to loose their fighting spirit even more... *")
        case 3:
            time.sleep(1)
            if player_stats["ammo"]>=10:
                if coinFlip()=="Pass":
                    print("PASS")
                    playsound("../sounds/gun1.mp3")
                    print("* You command your group to shoot at the beast... *")
                    time.sleep(1)
                    print("* it seems to run away in fear back into the trees... *")
                    player_stats["ammo"]-=10
                else:
                    print("FAIL")
                    playsound("../sounds/gun1.mp3")
                    print("* You command your group to shoot at the beast... *")
                    playsound("../sounds/gun2.mp3")
                    print("* As you shoot the beast you see it pouncing on your members... *")
                    player_stats["members"]-=3
                    gameover(player_stats)
                    print("*", player_stats["members"], "members left... *")
                    player_stats["morale"]-=1
                    print("* The group seems to loose their fighting spirit even more... *")
            else:
                print("* You reach for your weapons, but you're out of ammo... *")
                time.sleep(1)
                player_stats["members"]-=3
                gameover(player_stats)
                print("* The beast gets to a few of your group before fleeing... *")
                print("*", player_stats["members"], "members left... *")

#neutral encounters
def blockade(player_stats):
    print("* As your group marches through the snow, you come across a blockade... *")
    time.sleep(1)
    print("* It seems to be a bunch of cars and rubble, stacked upon each other... *")
    choice = int(input("What do you do?\n 1. Go around          2. Maybe this is a sign to rest for a bit          3. Target Practice (REQS AMMO)\n>> "))
    match choice:
        case 1:
            if coinFlip()=="Pass":
                print("PASS")
                time.sleep(1)
                print("* Even though your group was convinced it was an ambush, turns out you're safe... *")
                time.sleep(1)
                print("* The group seems to trust you a little more now *")
                player_stats["trust"]+=1
            else:
                print("* A group of bandits were waiting to ambush your group *")
                if player_stats["ammo"]>=30:
                    time.sleep(1)
                    print("* Your group raises their guns and begins to fire *")
                    playsound("../sounds/gun1.mp3")
                    if coinFlip()=="Pass":
                        print("PASS")
                        time.sleep(1)
                        print("* Your group effortlessly takes the bandits down and defends themselves... *")
                        player_stats["ammo"]-=30
                        time.sleep(1)
                        print("-30 ammo")
                    else:
                        print("FAIL")
                        time.sleep(1)
                        print("* Your group fights their hardest but they still take casualties... *")
                        player_stats["members"]-=5
                        gameover(player_stats)
                        player_stats["ammo"]-=30
                        time.sleep(1)
                        print("-30 ammo")
                        print("*",player_stats["members"],"member(s) left... *")
                else:
                    # No ammo to fight back with - the ambush just costs you members
                    print("* You have no ammo to fight back with... *")
                    time.sleep(1)
                    player_stats["members"]-=8
                    gameover(player_stats)
                    print("* The bandits overwhelm your group... *")
                    print("*",player_stats["members"],"member(s) left... *")
        case 2:
            if player_stats["fuel"]>=10:
                print("* Your group decides to take a well needed rest... *")
                time.sleep(1)
                print("* They start a big fire to heat themselves up *")
                time.sleep(1)
                print("-10 fuel")
                player_stats["fuel"]-=10
                player_stats["morale"]+=1
            else:
                print("* Your group decides to rest, however there's no fuel to burn *")
                player_stats["members"]-=1
                gameover(player_stats)
                time.sleep(1)
                print("* It seems one of the weaker members has fallen to frostbite *")
                time.sleep(1)
        case 3:
            if player_stats["ammo"]>=50:
                print("* One of your group members grabs their gun and shoots the cars out of rage... *")
                playsound("../sounds/gun2.mp3")
                print("* Others begin to join in... *")
                playsound("../sounds/gun1.mp3")
                if coinFlip()=="Pass":
                    print("PASS")
                    time.sleep(1)
                    print("* One of the bullets strikes the fuel tank of the cars... *")
                    time.sleep(1)
                    print("* A subtle spark turns the entire barricade into a fireball... *")
                    time.sleep(1)
                    print("* As your group cheers at the wreckage they caused, you can feel their fighting spirits ignite once more *")
                    print("* -40 ammo *")
                    player_stats["ammo"]-=40
                    player_stats["morale"]+=1
                else:
                    print("* As the gun fire dies down, the first shooter realises hes been shooting an empty gun for a while now... *")
                    time.sleep(1)
                    print("* You manage to calm them down and decide to just walk around the blockade... *")
                    player_stats["ammo"]-=30
                    player_stats["morale"]-=1
                    print("* The group's fighting sprit seems to die down just a little bit... *")
            else:
                print("* You don't have enough ammo for that... *")
                time.sleep(1)
                print("* You decide to just walk around instead... *")
def merchant_encounter(player_stats):
    print("* In the distance you spot a lone figure with a heavily laden sled... *")
    time.sleep(1)
    approach = input("Do you want to approach the merchant? (y/n)\n>> ").lower()
    if not approach.startswith("y"):
        print("* You decide to keep your distance and move on... *")
        return
    time.sleep(1)
    if player_stats["rep"] < 4:
        print("The Merchant: The Road knows who you are. Get lost...")
        return
    print("The Merchant: Aha, welcome.... Looking to trade?")
    time.sleep(1)
    choice = input("What do you do?\n 1. Open shop          2. Steal from the merchant          3. Quit\n>> ")
    match choice:
        case "1":
            merchant_shop(player_stats)
        case "2":
            print("* Whilst you are bargaining with the merchant, one of your members sneaks around and grabs some of his loot*")
            time.sleep(1)
            if coinFlip() == "Pass":
                print("PASS")
                random_loot(player_stats)
            else:
                print("FAIL")
                time.sleep(1)
                print("* The merchant catches them red-handed *")
                time.sleep(1)
                print("The Merchant: HEY! PUT THAT BACK!")
                player_stats["ammo"] -= 1
                playsound("../sounds/gun2.mp3")
                player_stats["rep"] -= 2
                time.sleep(1)
                print("-1 ammo")
                time.sleep(1)
                print("* You feel as if you've commited a great sin, how can anyone look at you the same... *")
        case "3":
            print("* You decide against it and walk away... *")

#positive encounters
def supply(player_stats):
    print("* As you stumble through the snow, you come across a large crate with a parachute attached... *")
    time.sleep(2)
    print("* As your group surrounds it its clear there's a a few supplies around the crash site... *")
    time.sleep(2)
    print("* The large crate seems to pry open, however its not clear if you can... *")
    if coinFlip()=="Pass":
        print("PASS")
        time.sleep(2)
        print("* Through all your efforts, the crate finally lifts open... *")
        random_loot(player_stats)
    else:
        print("FAIL")
        time.sleep(2)
        print("* Despite all your effort, the crate will not open... *")
        time.sleep(2)
        print("* You find comfort in the fact you still got something for free in this world... *")
        time.sleep(2)
    print("+ 20 ammo")
    player_stats["ammo"]-=20
def speech(player_stats):
    print("* As your group marches through the snow, you can tell their morale is low... *")
    time.sleep(1)
    print("* You turn around and raise your hand to halt them. *")
    time.sleep(1)
    print("* The wind blows from behind you as you stand in front of all your group *")
    time.sleep(1)
    print("* You open your mouth to say something... *")
    time.sleep(1)
    choice=int(input("What do you say?\n1. A speech to encourage their spirits          2. A speech that strengthens your bond with them           3. A speech that reminds them what they are fighting for\n>>  "))
    match choice:
        case 1:
            print("* The speech riles your group up, you feel their fighting spirit ignite once more... *")
            time.sleep(1)
            print("+1 Morale")
            player_stats["morale"]+=1
        case 2:
            print("* The speech reaches the hearts of many of your members, you feel as if they are your real family now.. *")
            time.sleep(1)
            print("+1 Trust")
            player_stats["trust"]+=1
        case 3:
            if coinFlip()=="Pass":
                print("PASS")
                time.sleep(2)
                print("The speech strikes the soul of your entire group. Their loyalty can be felt through the air")
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
def sing(player_stats):
    print("* As your group marches, the wind begins to howl... *")
    time.sleep(2)
    print("* The sounds of the winds and the sounds of walking combine and sound eerily similar to a popular song before all of this... *")
    time.sleep(2)
    print("* To pass the time, one of your group members begins to sing that very song... *")
    time.sleep(2)
    print("* More and more people join in, and soon, everyone is singing... *")
    time.sleep(2)
    player_stats["morale"]+=1
    print("+1 morale")
def cart(player_stats):
    print("* As your group continues on their journey, you come a crashed wooden cart... *")
    time.sleep(2)
    print("* It seems as if the wheel has came off. Whoever drove it took whatever he could hold and ran off... *")
    time.sleep(2)
    print("* Maybe its best if we just take what they left behind, not like they're using it anyways... *")
    time.sleep(2)
    random_loot(player_stats)
