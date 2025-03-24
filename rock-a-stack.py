from colorama import Fore, Back, Style
stacked=0 #number of stacked rings
ringStack=[] #empty list to be filled with lists of details for each ring, those being the color, diameter, and what the ring looks like on the stack.
red=["Red",9,"═════════"]
yellow=["Yellow",7,"═══════"]
green=["Green",5,"═════"]
blue=["Blue",3,"═══"]
cyan=["Cyan",1,"═"]
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
    print("Here are the rings you can put on the stack.")
    print("")
    counter=0 
    for i in freeRings:
        counter+=1
        if i[0]=="Red":
            print(Fore.RED,end="")
        elif i[0]=="Yellow":
            print(Fore.YELLOW,end="")
        elif i[0]=="Green":
             print(Fore.GREEN,end="")
        elif i[0]=="Blue":
            print(Fore.BLUE,end="")
        else:
            print(Fore.CYAN,end="")
        print (counter,": ",i[0],sep="")
        print(Fore.RESET)
        while True: #another input loop
            choice=(input("Input A again to choose a ring to add to the stack, input D to inspect a ring, or input X to return to the stack."))

def menuChoose():
    print("")
    choice=input("Input A to add a ring to the stack, input R to remove the top ring, input S to look at a specific ring, or input X to exit.")
    print("")
    if choice=="A" or choice=="a":
        if freeRings==[]:
            print("Sorry, there are no rings left!")
            menuChoose()
        else:
            pass

def drawStack():
    print("At the moment, the stack looks like this:")
    print(Fore.RESET+"    O    ")
    for i in range(5-stacked):
        print("    ║    ")
    print(Fore.RESET+"════╩════")


print(Fore.RESET+"Welcome to Rock-a-stack!")
drawStack()
menuChoose()

        