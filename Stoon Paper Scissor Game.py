import random
sum=0#winning points
l=0#loosintg points
tg=0
print("Stoon Paper Scissor Game")
print("\n")
t=int(input("Enter Turn Time :- "))
print("\n")
ct=random.choice(["stoon","paper","scissor"])
for i in range(t):
    u=input("Your Turn :- ")
    if(ct=="scissor" and u=="stoon"):
        print("You Win The Game")
        print("Computer = ",ct)
        print("\n")
        sum=sum+1
        continue
    elif(ct=="paper" and u=="stoon"):
        print("You Win The Game")
        print("Computer = ",ct)
        print("\n")
        sum=sum+1
        continue    
    elif(ct=="paper" and u=="scissor"):
        print("You Win The Game")
        print("Computer = ",ct)
        print("\n")
        sum=sum+1
        continue
    elif(ct=="stoon" and u=="scissor"):
        print("You Loose The Game")
        print("Computer = ",ct)
        print("\n")
        l=l+1
        continue    
    elif(ct=="scissor" and u=="paper"):
        print("You Loose The Game")
        print("Computer = ",ct)
        print("\n")
        l=l+1
        continue    
    elif(ct=="stoon" and u=="paper"):
        print("You Loose The Game")
        print("Computer = ",ct)
        print("\n")
        l=l+1
        continue    
    elif(ct=="stoon" and u=="stoon"):
        print(" The Game Tei")
        print("Computer = ",ct)
        print("\n")
        tg=tg+1
        continue    
    elif(ct=="scissor" and u=="scissor"):
        print("The Game Tei")
        print("Computer = ",ct)
        print("\n")
        tg=tg+1
        continue    
    elif(ct=="paper" and u=="paper"):
        print("The Game Tei")
        print("Computer = ",ct)
        print("\n")
        tg=tg+1
        continue    
print("Score Board ")
print("You Win The Match :- ",sum)
print("You Loose The Match :- ",l)
print("The Tei Match :- ",tg)
