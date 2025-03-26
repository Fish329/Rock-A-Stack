stacked=0 #number of stacked rings
ringStack=[] #empty list to be filled with lists of details for each ring, those being the color, diameter, what the ring looks like on the stack, and the escape code for the color.
red=["Red",9," ═════════ ","\x1b[31m"]
yellow=["Yellow",7,"  ═══════  ","\x1b[33m"]
green=["Green",5,"   ═════   ","\x1b[32m"]
blue=["Blue",3,"    ═══    ","\x1b[34m"]
cyan=["Cyan",1,"     ═     ","\x1b[96m"]
freeRings=[red,yellow,green,blue,cyan] #list of rings that havent been added to the stack

def empty(): #check if the stack is empty.
    if stacked==0:
        return True
    else:
        return False

def size(): #return the number of rings on the stack.
    return stacked

def top(): #return the top ring.
    return ringStack[0]

def push(a): #pushes an element onto the top of the stack.
    ringStack.insert(0,a)

def addRing():
    global stacked
    print("Here are the rings you can put on the stack.")
    print("")
    counter=0 
    for i in freeRings:
        counter+=1
        print(i[3],end="")
        print (counter,": ",i[0],sep="")
        print("\x1b[0m",end="")
    print("")
    while True: #another input loop
        choice=(input("Input the number of a ring you would like to inspect. "))
        try:
            int(choice) #make sure the choice is a number. If not, ask again
        except:
            print("ERROR: please choose a number from the list given.")
            continue
        choice=int(choice)
        if choice>len(freeRings) or choice<1: #also make sure the choice is within range
            print("ERROR: please choose a number from the list given.")
            continue
        break
    choice-=1
    print("") #Inspection screen
    print("### Ring Details:",freeRings[choice][0],"###")
    print("A colored plastic ring. it looks like this:")
    print(freeRings[choice][3])
    print("〇") #They're all rings, so I can get away with just recoloring the same sprite
    print("\x1b[0m"+"Diameter in units: ",freeRings[choice][1],sep="")
    print("---------------------------------------------")
    print("")
    while True: #input loop
        choose=input("Would you like to add this ring to the stack? (Y/N) ") #"choice" and "choose" have seperate usages here
        if choose=="y" or choose=="Y":
            print("You put the",freeRings[choice][0],"ring onto the stack.")
            push(freeRings[choice])
            freeRings.pop(choice)
            stacked=stacked+1
            print("")
            drawStack()
            menuChoose()
        elif choose=="n" or choose=="N":
            print("")
            addRing()
        else:
            print("ERROR: please choose Y or N.")
            continue



def menuChoose():
    global stacked
    print("")
    choice=input("Input A to add a ring to the stack, input R to remove the top ring, or input X to exit. ")
    print("")
    if choice=="a" or choice=="A":
        if freeRings==[]: #If there aren't any rings left, don't bother
            print("Sorry, there are no rings left!")
            menuChoose()
        else:
            addRing()
    elif choice=="r" or choice=="R":
        if stacked==0:
            print("There are no rings on the stack.")
            menuChoose()
        else:
            print("You remove the",top()[0],"ring.")
            freeRings.append(top())
            ringStack.pop(0)
            stacked=stacked-1
            drawStack()
            menuChoose()
    elif choice=="x" or choice=="X":
        print("See you later!")
        exit()
    else:
        print("ERROR: please choose from the list given.")
        menuChoose()

def drawStack():
    print("At the moment, the stack looks like this:")
    print("")
    print("\x1b[0m"+"     O    ")
    print("     ║    ")
    for i in range(5-stacked):
        print("     ║    ")
    for j in ringStack:
        print(j[3],end="")
        print(j[2])
    print("\x1b[0m"+"═════╩═════")


print("\x1b[0m"+"Welcome to Rock-a-stack!")
drawStack()
menuChoose()

        