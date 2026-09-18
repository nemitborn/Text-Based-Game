import time
titleCard="""
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
print(titleCard)
time.sleep(2)
def tutorial():
    print("WINTER ROAD is a text based game where you will need to guide your group and manage your resources whilst traveling across The Road")
    time.sleep(2)
    print("Every day there will be 3 encounters you have to face. You will be presented with different options that correspond to a number")
    time.sleep(2)
    print("Use the number keys (1-9) to choose which action you would like to do")
    time.sleep(2)
    print("Use the ENTER key to confirm your choice and the Backspace key to delete whatever number you typed")
    time.sleep(2)
    print("Some encounters will require you to choose the correct side on a coinflip")
    time.sleep(2)
    print("Get it wrong and your group faces consequences, get it right and you'll get a favourable outcome")
    time.sleep(2)
input("Welcome to WINTER ROAD, would you like a tutorial to begin?\n")
time.sleep(2)
if "Yes"or"yes"or"y"or"ues":
    tutorial()
    repeat=("You got all that? or do you need me to repeat it again")
    while repeat=="Yes"or"yes"or"y"or"ues":
        print("listen up well this time...")
        time.sleep(3)
        tutorial()
    else:
        print("cool")
