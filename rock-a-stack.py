stacked=0 #number of stacked rings.
ringStack=[] #empty list to be filled with lists of details for each ring, those being the color, diameter, what the ring looks like on the stack, and the escape code for the color.
cRESET="\033[0m"
cRED="\x1b[31m"
cYELLOW="\x1b[33m"
cGREEN="\x1b[32m"
cBLUE="\x1b[34m"
cCYAN="\x1b[96m"
red=["Red",9," ═════════ ",cRED]
yellow=["Yellow",7,"  ═══════  ",cYELLOW]
green=["Green",5,"   ═════   ",cGREEN]
blue=["Blue",3,"    ═══    ",cBLUE]
cyan=["Cyan",1,"     ═     ",cCYAN]

freeRings=[red,yellow,green,blue,cyan] #list of rings that havent been added to the stack

def empty(stacked): #check if the stack is empty.
    if stacked==0:
        return True
    else:
        return False

def size(stacked): #return the number of rings on the stack.
    return stacked

def top(): #return the top ring.
    return ringStack[0]

def push(data): #pushes an element onto the top of the stack.
    ringStack.insert(0,data) #this line is altering an array. When there is already an item at index 0, it gets moved over to index 1, and the item at index 1 gets moved over to index 2, etc. This works because arrays can be changed and moved around.
def pop(): #removes the top item of the stack.
    ringStack.pop(0)

def addRing(stacked): #Menu for choosing rings
    print("")
    counter=0 
    for i in freeRings: #Print out rings that havent been added to the stack yet
        counter+=1
        print(i[3],end="")
        print (counter,": ",i[0],sep="")
        print(cRESET,end="")
    print("")
    while True: #another input loop
        choice=(input("Input the number of a ring you would like to inspect. ")) #ask user for ring number
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
    print("### Ring Details:",freeRings[choice][0],"###") #print out the name of the ring
    print("A colored plastic ring. it looks like this:")
    print(freeRings[choice][3],end="")
    print("〇") #They're all rings, so I can get away with just recoloring the same sprite
    print(cRESET+"Diameter in units: ",freeRings[choice][1],sep="")
    print("It looks like this on the stack:")
    print(freeRings[choice][3],end="")
    print(freeRings[choice][2])
    print(cRESET,end="")
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
            drawStack(stacked)
            menuChoose(stacked)
        elif choose=="n" or choose=="N":
            print("")
            addRing(stacked)
        else:
            print("ERROR: please choose Y or N.")
            continue



def menuChoose(stacked): #Decision screen, shows up under the complete stack
    print("")
    choice=input("Input A to add a ring to the stack, input R to remove the top ring, or input X to exit. ")
    print("")
    if choice=="a" or choice=="A": #add a ring to the stack
        if freeRings==[]: #If there aren't any rings left, don't bother
            print("Sorry, there are no rings left!")
            menuChoose(stacked)
        else:
            addRing(stacked)
    elif choice=="r" or choice=="R": #remove a ring from the stack
        if stacked==0: #if there are no rings on the stack, don't bother
            print("There are no rings on the stack.")
            menuChoose(stacked)
        else:
            print("You remove the",top()[0],"ring.") #Otherwise pop the top ring
            freeRings.append(top())
            pop()
            stacked=stacked-1
            drawStack(stacked)
            menuChoose(stacked)
    elif choice=="x" or choice=="X": #exit the program
        print("See you later!")
        exit()
    else:
        print("ERROR: please choose from the list given.")
        menuChoose(stacked)

def drawStack(stacked): # Image of the stack
    print("At the moment, the stack looks like this:")
    print("")
    print(cRESET+"     O    ") #Top of the stack
    print("     ║    ") #I think one extra space looks nice. 
    for i in range(5-stacked): #print empty spaces for the amount of empty spaces on the stack
        print("     ║    ")
    for j in ringStack: #Print rings in color
        print(j[3],end="") #get ring's color
        print(j[2]) #print ring
    print(cRESET+"═════╩═════")

print("")
print(cRESET+"Welcome to Rock-a-stack!")
drawStack(stacked)
menuChoose(stacked)

        
