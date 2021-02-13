import random
rn=random.randint(1,10)
sum=0
print("Enter Number Between 1 to 10")    
for i in range(5):
    num=int(input("Enter Youe Number :- "))
    sum=sum+1
    if(num>10):
        print("Enter Number Again")
        continue
    if(num==rn):
         print(sum," ","You Win The Game")
         print("   ","Your Number is ",num)
         print("   ","My Number is ",rn)
         break
    elif(num<10 and (num+1 or num+2)==rn):
        print(sum," ","Very Close to win")
        print("   ","Your Number is ",num)
        print("   ","My Number is ",rn)
    elif(num<10 and (num+3 or num+4)==rn):
        print(sum," ","Close to win")
        print("   ","Your Number is ",num)
        print("   ","My Number is ",rn)
    elif(num<10 and (num+5 or num+6 or num+7 or num+8 or num+9)==rn):
        print(sum," ","Far to win")
        print("   ","Your Number is ",num)
        print("   ","My Number is ",rn)
    else:
        print(sum," ","Very Far to win")
    print("\n")
