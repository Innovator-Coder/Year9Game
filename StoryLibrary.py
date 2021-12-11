import random
import time
import playsound
import termcolor
import os

whitestar = chr(9734)
blackstar = chr(9733)

#Michael Chen's Function
def clearConsole():
    clear = lambda: os.system('clear')
    clear()

def helper():
    help = input("Help Menu:' \n\nSummary of Game: The Escape, The Dragons Den, The ThunderDome.\nIf you would like to check your score, input 'score'\n If you get 10 points, you will be ranked as a novice.\n If you get 20 points, you will be ranked as a VIP\n If you get 30 points you will be ranked as a VIP+\n If you get 40 points you will be ranked as MVP\n If you get 50 points you will be ranked as MVP+\n If you get 60 points you will be ranked as MASTER\nIf you would like the history of your story to be deleted and restarted input 'delete'\nTo check your rank, type 'rank'\n\n\nHave fun! : ")
    time.sleep(2)
    if "score" in help.lower():
        wonnumber1 = int(input("How many times you have won a game (meaning you got every question right)? 'make sure to answer with a number like 1 or 2': "))
        losenumber1 = int(input("How many times you have lost a game (meaning you didn't get every question right)? 'make sure to answer with a number like 1 or 2': "))
        score1 = wonnumber1*10 -losenumber1*5
        print(score1)

    if "rank" in help.lower():

        wonnumber2 = int(input("How many times you have won a game (meaning you got every question right)? 'make sure to answer with a number like 1 or 2': "))
        losenumber2 = int(input("How many times you have lost a game (meaning you didn't get every question right)? 'make sure to answer with a number like 1 or 2': "))
        score2 = wonnumber2*10 -losenumber2*5        

        time.sleep(2)

        if score2 < 10:
            print("No Rank")
        elif score2 < 20:
            print("Novice")
        elif score2 < 30:
            print("VIP")
        elif score2 < 40:
            print("VIP+")
        elif score2 < 50:
            print("MVP")   
        elif score2 < 60:
            print("MVP+")
        elif score2 < 70:
            print("Master!") 

    

    if "delete" in help.lower():
        #Michael Chen's Function is below
        clearConsole()


def theThunderDome():
    playsound.playsound("Thunder.mp3")
    print("I have chosen for you... The.... THUNDER DOME")
    time.sleep(1)
    guardans = input("Do you want to talk to the Guard? (type 'yes' or 'no')\n:")
    if "yes" in guardans.lower():
        print("I am Marcus, the guard of the THUNDER DOME. Be thankful you have requested for my help: When you're getting colder, you're actually getting hotter... ")
        time.sleep(3) 
    elif "no" in guardans.lower():
        print("Very well then, be advised that it will be very challenging")
        time.sleep(3) 
    elif "help" in guardans.lower():
        helper()
    else:
        print("Sorry I dont understand what you're trying to say :(, try again, I'll take it as a no")
        time.sleep(3) 

    print("Here is your puzzle! Grab a friend and try to crack it!") 
    time.sleep(3)       
    print("The challenge is...")
    time.sleep(2)
    print("Find the Thunder wand! It is one of 8 rooms, one of them has it! Guess which one it is...")
    time.sleep(3)
    print("All the rooms are at different temperatures.")

    print("Room 1 is at 35 Degrees Celsius")
    time.sleep(1)
    print("Room 2 is at 42 Degrees Celsius")
    time.sleep(1)
    print("Room 3 is at 28 Degrees Celsius")
    time.sleep(1)
    print("Room 4 is at -32 Degrees Celsius")
    time.sleep(1)
    print("Room 5 is at -15 Degrees Celsius")
    time.sleep(1)
    print("Room 6 is at 6 Degrees Celsius")
    time.sleep(1)
    print("Room 7 is at 5 Degrees Celsius")
    time.sleep(1)
    print("Room 8 is at -5 Degrees Celsius")
    time.sleep(1)
    roomans = input("Enter the Room (like this 'Room 1' or 'Room 2'): ")
    if "Room 4" in roomans.lower():
        print("Correct!")
    elif "help" in roomans.lower():
        helper()
    else:   
        print("Incorrect, but it's okay! No problem, lets try again!")



    print("Good Job! Lets Battle the Boss, the Thunder Giant!")
    time.sleep(1)
    print("The Thunder Giant is here! He says 'Get ready to get defeated!' We wont let that happen! ")            
    time.sleep(2)
    print("You will have to write words as much as possible and as fast as possible to use your wand until he is defeated!")
    time.sleep(1)
    attack1 = input("Write 'attack': ")
    if "attack" in attack1.lower():
        print("Good Job! You dealt a lot of damage!")
    elif "help" in attack1.lower():
        helper()
    else: 
        print("It's okay, lets move to the next word!")
        time.sleep(1)
    attack2 = input("Write 'Wand': ")
    if "wand" in attack2.lower():
        print("Holy Moly! You're so good at this!")
        time.sleep(1)
    elif "help" in attack2.lower():
        helper()
    else: 
        print("It's okay, lets move to the next word!")

    attack3 = input("Write 'Wizard': ")
    if "wizard" in attack3.lower():
        print("Holy Smokes! You defeated him! Good Job!")
        time.sleep(1)
    elif "help" in attack3.lower():
        helper()
    else: 
        print("It's okay, learning to type is all about improvement! Lets try a different game!")
        time.sleep(3)
    print("Lets try out another game! What about a random game!")
    time.sleep(3)
    advthunder = [theDragonsDen,theEscape]
    advthunderrand = random.choice(advthunder)
    advthunderrand()
    







def theDragonsDen():
    print("We have chosen for you... The.... DRAGONS DEN")
    time.sleep(2)
    playsound.playsound("gong.mp3")
    time.sleep(1)
    print("We stumble into his cave, HIS DEN, and he is ANGRY! We need to try to talk to him first before doing anything else!")
    time.sleep(3)
    calmdragonans = input("You should say something nice to try to calm the dragon down! What will you say? : ")
    if "help" in calmdragonans:
        helper()
    time.sleep(1)
    print("The dragon responds: Pff... just a bunch of kids LYING! And you're trying to steal my things!")
    time.sleep(2)
    print("I guess we can't do anything, lets challenge the dragon to a battle! I'll tell him!")
    time.sleep(2)
    print("He responds: Well what kind of battle?")
    time.sleep(2)
    print("How about a math battle?")
    time.sleep(1)
    print("The dragon responds: Sure! Get ready to be defeated!")
    time.sleep(2)
    print("We won't let that happen! Lets answer some of his math questions!")
    time.sleep(2)
    math1 = int(input("What number is the minute hand on when the time is 2:30 (make sure you're answer is only a number like 1 or 9): "))
    if math1 == 6:
        print("Correct! Let's try another question!")
    else:
        print("Incorrect. No problem though! Let's try another question!")
    time.sleep(2)
    math2 = int(input("Whats 4 x 5? (make sure you're answer is only a number like 1 or 9): "))
    if math2 == 20:
        print("Correct! Lets move on to the next question!")    
    else:
        print("Incorrect. Lets try another one!")
    math3 = int(input("How much money is 5 dimes and 2 quarters? (write the answer in cents): "))
    if math3 == 100:
        print("Correct! One last question!")
    else:
        print("Incorrect. Lets try one last one!")
    math4 = input("Does a backpack weight more similar to 7 grams, 7 kilograms, or 7 miligrams? : ")
    if "kilograms" in math4:
        print("Wow good job! You're right! Let's try another game!")
    elif "help" in math4:
        helper()
    else:
        print("Incorrect. It's alright! Let's try another questions!")
    advdragons = [theThunderDome,theEscape]
    advdragonsrand = random.choice(advdragons)
    advdragonsrand()











def theEscape():
    print("We have chosen for you... The.... The ESCAPE")
    time.sleep(1)
    playsound.playsound("bomb.mp3")
    theEscapeAns = input("You need to escape the BOMB!!! Do you want a hint? ")
    if "yes" in theEscapeAns.lower():
        print("Good job for picking this option! I'm Drake! You'll be greatful once I tell you you're third clue in the DARK...")
    elif "help" in theEscapeAns.lower():
        helper()
    else:
        print("Very well... Proceed as you like :|")
    print("Well lets begin! There are 15 Strings, and 2 of them need to be cut, which ones will you chose (answer the 2 numbers exactly like: 2 and 3)?")

    rod ="||"

    printRod = termcolor.colored(rod,'white','on_grey')

    wire1 ="======================"
    wire2 ="======================"
    wire3 ="======================"
    wire4 ="======================"
    wire5 ="======================"
    wire6 ="======================"
    wire7 ="======================"
    wire8 ="======================"
    wire9 ="======================"
    wire10="======================"
    wire11="======================"
    wire12="======================"
    wire13="======================"
    wire14="======================"
    wire15="======================"

    printWire1 = termcolor.colored(wire1, 'red', 'on_white')
    printWire2 = termcolor.colored(wire2, 'green', 'on_white')
    printWire3 = termcolor.colored(wire3, 'yellow', 'on_white')
    printWire4 = termcolor.colored(wire4, 'blue', 'on_white')        
    printWire5 = termcolor.colored(wire5, 'magenta', 'on_white')
    printWire6 = termcolor.colored(wire6, 'cyan', 'on_white')
    printWire7 = termcolor.colored(wire7, 'grey', 'on_white')
    printWire8 = termcolor.colored(wire8, 'green', 'on_white')
    printWire9 = termcolor.colored(wire9, 'yellow', 'on_white')
    printWire10 = termcolor.colored(wire10, 'blue', 'on_white')
    printWire11 = termcolor.colored(wire11, 'magenta', 'on_white')
    printWire12 = termcolor.colored(wire12, 'cyan', 'on_white')
    printWire13 = termcolor.colored(wire13, 'red', 'on_white')
    printWire14 = termcolor.colored(wire14, 'green', 'on_white')
    printWire15 = termcolor.colored(wire15, 'yellow', 'on_white')

    print("1 -->    " + rod + printWire1 + rod)
    time.sleep(0.5)
    print("2 -->    " + rod + printWire2 + rod)
    time.sleep(0.5)
    print("3 -->    " + rod + printWire3 + rod)
    time.sleep(0.5)
    print("4 -->    " + rod + printWire4 + rod) 
    time.sleep(0.5)   
    print("5 -->    " + rod + printWire5 + rod)
    time.sleep(0.5)   
    print("6 -->    " + rod + printWire6 + rod)
    time.sleep(0.5)   
    print("7 -->    " + rod + printWire7 + rod)
    time.sleep(0.5)   
    print("8 -->    " + rod + printWire8 + rod)
    time.sleep(0.5)   
    print("9 -->    " + rod + printWire9 + rod)
    time.sleep(0.5)   
    print("10 -->   " + rod + printWire10 + rod)
    time.sleep(0.5)   
    print("11 -->   " + rod + printWire11 + rod)
    time.sleep(0.5)   
    print("12 -->   " + rod + printWire12 + rod)
    time.sleep(0.5)   
    print("13 -->   " + rod + printWire13 + rod)
    time.sleep(0.5)   
    print("14 -->   " + rod + printWire14 + rod)
    time.sleep(0.5)   
    print("15 -->   " + rod + printWire15 + rod)
    time.sleep(0.5)   
    
    theEscapeWires = input("Answer: ")
    if "3 and 7" in theEscapeWires.lower() or "7 and 3" in theEscapeWires.lower():
        print("Good job, you have diffused the bomb! Good job at taking a risk!")
    elif "help" in theEscapeWires.lower():
        helper()
    else:
        print("The bomb has exploded, but everyone was safe due to collaboration and you taking a risk for keeping them safe! It's all right! Let's try another game and we can come back here for another try.")
    
    advescape = [theThunderDome,theDragonsDen]
    advescaperand = random.choice(advescape)
    advescaperand()


        


def randomStory():
    print("The Random Adventure is.... (Drum Roll Please...Come on...)")
    playsound.playsound("drumroll.mp3")
    time.sleep(3)
    functionList = [theThunderDome,theDragonsDen,theEscape]
    adventure = random.choice(functionList) 
    adventure()


