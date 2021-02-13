import random
print("Children Math Quiz Game")
q=0
qp=0
name=input("Enter Player Name : ")
for i in range(5):
  if(q<=5):
      qv=random.randint(10,99)
      qv1=random.randint(10,99)
      print("Q.No.",q+1)
      print(" ",qv)
      print("+",qv1)
      print("_"*42)
      u=int(input(""))
      print("_"*42)
      if(u==(qv+qv1)):
          print("Right Answer")
          qp=qp+1
      else:
          print("Wrong Answer","Right Answer is ",(qv+qv1))
      print("_"*42)
      q=q+1
      if(q==5):
        for i in  range(999):
            qv=random.randint(10,99)
            qv3=random.randint(10,99)
            if(qv>qv3):
                print("Q.No.",q+1)
                print(" ",qv)
                print("-",qv3)
                print("_"*42)
                u=int(input(""))
                print("_"*42)
                if(u==(qv-qv3)):
                    print("Right Answer")
                    qp=qp+1
                else:
                    print("Wrong Answer","Right Answer is ",(qv-qv3))
                q=q+1
                print("_"*42)
                if(q==10):
                    break
        for i in  range(5):
            qv=random.randint(10,99)
            qv3=random.randint(1,9)
            print("Q.No.",q+1)
            print(" ",qv)
            print("* ",qv3)
            print("_"*42)
            u=int(input(""))
            print("_"*42)
            if(u==(qv*qv3)):
                print("Right Answer")
                qp=qp+1
            else:
                print("Wrong Answer","Right Answer is ",(qv*qv3))
            print("_"*42)
            q=q+1
            if(qp==15):
                    break
        for i in range(5):
            qv=random.randint(10,99)
            qv3=random.randint(1,9)
            print("Q.No.",q+1)
            print(" ",qv)
            print("/ ",qv3)
            print("_"*42)
            u=int(input(""))
            print("_"*42)
            if(u==(int(qv/qv3))):
                print("Right Answer")
                qp=qp+1
            else:
                print("Wrong Answer","Right Answer is ",(int(qv/qv3)))
            print("_"*42)
            q=q+1
print("Name is :",name.capitalize())
print("Total Question is :",q)        
print("Total Right Answer is :",qp)
print("Total Wrong Answer is :",q-qp)
