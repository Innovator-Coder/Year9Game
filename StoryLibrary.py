import random
import time
import playsound
import termcolor

whitestar = chr(9734)
blackstar = chr(9733)

def theThunderDome():
    playsound.playsound("Thunder.mp3")
    print("I have chosen for you... The.... THUNDER DOME")
    time.sleep(1)
    guardans = input("Do you want to talk to the Guard? (type 'yes' or 'no')\n")
    if "yes" in guardans.lower():
        print("I am Marcus, the guard of the THUNDER DOME. Be thankful you have requested for my help: When you're getting colder, you're actually getting hotter... ")
        time.sleep(3) 
    elif "no" in guardans.lower():
        print("Very well then, be advised that it will be very challenging")
        time.sleep(3) 
    elif "score" in guardans.lower():
        print(whitestar + whitestar + whitestar)
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
    if "Room 4" in roomans:
        print("Correct!")

    elif "score" in roomans:
        print(whitestar + whitestar + whitestar)
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
    elif "score" in roomans:
        print(whitestar + whitestar + whitestar)
    else: 
        print("It's okay, lets move to the next word!")
        time.sleep(1)
    attack2 = input("Write 'Wand': ")
    if "wand" in attack2.lower():
        print("Holy Moly! You're so good at this!")
        time.sleep(1)
    elif "score" in roomans:
        print(whitestar + whitestar + whitestar)
    else: 
        print("It's okay, lets move to the next word!")

    attack3 = input("Write 'Wizard': ")
    if "wizard" in attack2.lower():
        print("Holy Smokes! You defeated him! Good Job!")
        time.sleep(1)
    elif "score" in roomans:
        print(whitestar + whitestar + blackstar)
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
    advdragons = [theThunderDome,theEscape]
    advdragonsrand = random.choice(advdragons)
    advdragonsrand()


def theEscape():
    print("We have chosen for you... The.... The ESCAPE")
    time.sleep(1)
    playsound.playsound("bomb.mp3")
    print("You need to escape ")
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

