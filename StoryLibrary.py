import random
import time


def theThunderDome():
    print("I have chosen for you... The.... THUNDER DOME")
    time.sleep(1)
    guardans = input("Do you want to talk to the Guard?\n")
    if "yes" in guardans:
        print("I am Marcus, the guard of the THUNDER DOME. Be thankful you have requested for my help")
    elif "no" in guardans:
        print("Very well then, be advised that it will be very challenging ")
    

def theDragonsDen():
    print("We have chosen for you... The.... DRAGONS DEN")
    time.sleep(1)

def theEscape():
    print("We have chosen for you... The.... The ESCAPE")
    time.sleep(1)


def randomStory():
    print("The Random Adventure is.... (Drum Roll Please...Come on...)")
    #Insert Drum Roll Sound here
    time.sleep(3)
    functionList = [theThunderDome,theDragonsDen,theEscape]
    adventure = random.choice(functionList) 
    adventure()

