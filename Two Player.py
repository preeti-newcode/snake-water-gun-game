import random

def Choose(l):
    random.shuffle(l)
    print("\n-----------?----------->_<--------------?-----------------")
    p1=l[int(input("Player 1: Choose between 0 to 2: "))]
    print("-----------?----------->_<--------------?-----------------\n")
    random.shuffle(l)
    print("-----------?----------->_<--------------?-----------------")
    p2=l[int(input("Player 2: Choose between 0 to 2: "))]
    print("-----------?----------->_<--------------?-----------------\n")
    return p1,p2

def Result(a,b):
    print("----------------------------------------------------------")
    print(f"Player 1st:{a}\nPlayer 2nd:{b}")
    print("----------------------------------------------------------\n")
    if a==b:
        return 0
    else:
        if a=='Snake':
            if b=='Water':
                return 1
            else:
                return 2
        elif a=='Water':
            if b=='Gun':
                return 1
            else:
                return 2
        elif a=='Gun':
            if b=='Snake':
                return 1
            else:
                return 2

p1_marks={"Win":0,"Loss":0,"Tie":0}
p2_marks={"Win":0,"Loss":0,"Tie":0}

option=['Snake','Water','Gun']
print("Options:")
for x in option:
    print(x,end='\t')
print()
    
while True:
    
    p1,p2=Choose(option)
    
    value=Result(p1,p2)
    
    if value==0:
        p1_marks['Tie']=p1_marks['Tie']+1
        p2_marks['Tie']=p2_marks['Tie']+1
        print("Its a Tie")
    elif value==1:
        p1_marks['Win']=p1_marks['Win']+1
        p2_marks['Loss']=p2_marks['Loss']+1
        print("Player 1 Won")
    else:
        p1_marks['Loss']=p1_marks['Loss']+1
        p2_marks['Win']=p2_marks['Win']+1
        print("Player 2 Won")
    
    print("----------------------------------------------------------")    
    if input("Continue?:(yes/no) ").lower()=='yes':
        continue
    else:
        print("\n----------------------------------------------------------")
        print("----------------------------------------------------------")
        print(f"Result\n")
        print("Player 1")
        for x in p1_marks:
            print(f"{x} => {p1_marks[x]}")
        print()
        print("Player 2")
        for x in p2_marks:
            print(f"{x} => {p2_marks[x]}")
        break
