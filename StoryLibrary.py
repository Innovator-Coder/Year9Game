import random
import time

storynames = ["Adventure 1","Adventure 2","Adventure 3"]

def adventure1():
    print("this is an adventure 1.")

adv1 = adventure1

def adventure2():
    print("this is an adventure 2.")

adv2 = adventure2

def adventure3():
    print("this is an adventure 3.")

adv3 = adventure3

randnum = random.randint(0,2)

def randomStory():
    print("The Random Adventure is.... (Drum Roll Please...Come on...)")
    time.sleep(1)
    print(storynames[randnum])
    functionList = [adv1,adv2,adv3]
    functionList[randnum]