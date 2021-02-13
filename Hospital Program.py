# Package and Module and Function
from datetime import date
import random
import numpy as np
#Hospital Maintain Program
f=open('hd.txt','a')
f.writelines("Hospital Data Entry")
f.writelines("\n")
f.writelines("Shrivastav's Hospital")
f.writelines('\n')
print("            Shrivastav's Hospital")
doa=(date.today())
f.writelines("Date :"+str(doa)+"\n")
f.writelines('\n')
print("Date :",doa)
name=[]
sex=[]
st=["Male","Female"]
age=[]
f_n=[]
m_n=[]
r_No=[]
day=[]
b=0
print(day)
for i in range(1):
    
    print("S.NO :",i+1)
    f.writelines("S.no :"+str(i+1))
    f.writelines('\n')
   
    
    n=input("Enter Name : ")
    f.writelines("Name : "+str(n.capitalize()))
    f.writelines('\n')
    name.append(n.capitalize())
    
    
    S=input("Enter Sex : ")
    s=S.upper()
    if(s=="M"):
        f.writelines("Sex : "+str(st[0]))
        sex.append(st[0])
        f.writelines('\n')
    elif(s=="F"):
        f.writelines("Sex : "+str(st[1]))
        sex.append(st[1])
        f.writelines('\n')

    
    a=input("Enter age : ")
    f.writelines("Age : "+str(a))
    age.append(a)
    f.writelines('\n')
    
    
    f_name=input("Enter F.Name : ")
    f.writelines("Father Name : "+str(f_name.capitalize()))
    f.writelines('\n')
    f_n.append(f_name.capitalize())
    
    
    m_name=input("Enter M.Name : ")
    f.writelines("Mother Name : "+str(m_name.capitalize()))
    f.writelines('\n')
    m_n.append(m_name.capitalize())
    
    
    r_no=(random.randint(0,9999999))
    l=r_no in r_No
    if(l==True):
        continue
    else:
        print("Registration Number : ",r_no)
        r_No.append(r_no)
        f.writelines("Revservation No : "+str(r_no))
        f.writelines('\n')
    
    
    dod=input("Date of Discharge : ")
    f.writelines("Date of Discharge : "+dod+"\n")
    days=(np.datetime64(dod) - np.datetime64(doa))
    dy=(str(days)[0:2])
    day.append(dy)
    td=int((day[int(b)]))
    
    print("Billing : ")
    f.writelines("Billing : "+"\n")
    ta=td*1300
    gst=int(int(ta)*8/100)
    f.writelines("Amount : "+str(ta)+"\n")
    f.writelines("GST : "+str(gst)+"\n")
    o=input("Opration info :")
    if(o=="y"):
        oc=5300
        ta=ta+oc
        f.writelines("Bill with opration : "+str(ta)+"\n")
    TA=gst+ta
    f.writelines("Total Amount : "+str(TA)+"\n")
    f.writelines("-"*10)
    
    b=b+1
    
   
print(name)
print(age)
print(sex)
print(f_n)
print(m_n)
print(r_No)
print("Total Days in Hospital : ",dy)
print("Amount : ",ta)
print("GST :",gst)
print("Total Bill Amount :",TA)
