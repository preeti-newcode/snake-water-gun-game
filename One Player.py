from random import randint,shuffle

#Game Result Function
def Game(value,user):
    result=0
    if value==user:
        result=2
    
    elif value=="snake":
        if user=="water":
            result=0
        else:
            result=1
    
    elif value=="water":
        if user=="gun":
            result=0
        else:
            result=1
    
    elif value=="gun":
        if user=="snake":
            result=0
        else:
            result=1
    
    if result==1:
        rank["Wins"]=rank["Wins"]+1
        print("You WON\nCongratulation 👏 👏 👏 👏")
    elif result==2:
        rank["Tie"]=rank["Tie"]+1
        print("Its a TIE\nThis is unbelievable 😱!")
    else:
        rank["Losses"]=rank["Losses"]+1
        print("You lose, Computer win\nBetter Luck next time :)")

#Extra Note
print("----------------------------------------------")
print("Note:Enter STOP to end Game")
print("----------------------------------------------\n")
rank={"Wins":0,"Losses":0,"Tie":0}

#Main Body
while True:
    choice=randint(0,2)
    value=["snake","water","gun"]
    shuffle(value)
    
    print("----?---?---->_<---------?---?-----")
    user=input("\nSnake,Water,Gun\nChoose one:")
    user=user.lower()
    
    if user not in value:
        print("----------------------------------------------")
        print("\nLooks like You want to Exit\n\tIt was Fun\n\t\tBYE >-<")
        print("----------------------------------------------")
        print("Result\n")
        for x in rank:
            print(x,"=",rank[x])
        break
    
    print("----------------------------------------------")
    print(f"\nYour choice:{user.upper()}\nComputer choice:{value[choice].upper()}")
    print("----------------------------------------------\n")
    
    Game(value[choice],user)

