def uc(a,b):
    c=a*b
    return(int(c))

import datetime
import timedelta
import numpy as np
#progran Start from Here
print(" "*8,"BSES Rajdhani Limited")
hn=[]
hadd=[]
cn=[]
cano=[]
unit=[]
cano=[]
mt=[]
v=0
ca_no=15001
f=open('bses_data.txt','a')
f.write("-"*42)
f.write("Working Date : ")
f.write(str(datetime.date.today()))
f.write("\n")
f.writelines("-"*42)
for i in range(2):
    today = datetime.date.today()
    on=input("Bill Holder Name ")
    f.write("Meter Holder Name : ")
    f.write(on.capitalize())
    f.write("\n")
    
    add=input("Enter Address ")
    f.write("Address : ")
    f.write(add.capitalize())
    f.write("\n")
    
    for i in range(2):
        ph=input("Enter Contact no. :")
        lph=len(ph)
        if(lph==10):
            cn.append(ph)
            f.write("Contact No. ")
            f.writelines(ph)
            f.writelines("\n")
    
            break
        else:
            continue
    
    for i in range(2):
        u=int(input("Enter Used Units :"))
        if(u<=200):
            hur=3
            break
        elif(u>=201 and u<=400):
            hur=4.50
            break
        elif(u>=401 and u<=800):
            hur=6.50
            break
        elif(u>=800 and u<=1200):
            hur=7.00
            break
        elif(u>=1201):
            hur=7.50
            break
        elif(u>="a " or "A" and u<="z" or "Z"):
            continue
        f.write("Used Unit in Month : ")
        f.write(str(u))
        f.write("\n")
    
    dm=(np.datetime64("2020-09-03") - np.datetime64(today))
    h=str(dm)
    f.write("Days of Bill : ")
    f.writelines(h)
    f.write("\n")
    
    for i in range(2):
        mtu=input("Enter Meter Type :")
        if(mtu=="H" or mtu=="h"):
            mt.append("Home")
            f.write("Meter Type : ")
            f.write("Home")
            f.write("\n")
            break
        elif(mtu=="S" or mtu=="s"):
            mt.append("Shop")
            f.write("Meter Type : ")
            f.write("Shop")
            f.write("\n")
            break
    today = datetime.date.today()
    new = datetime.date.today() + datetime.timedelta(20)        
    f.write("Date of Bill : ")
    f.write(str(today))
    f.write("\n")
    f.write("Due Date : ")
    f.write(str(new))
    f.write("\n")     
            
    hn.append(on)
    hadd.append(add)
    unit.append(u)
    ca_no=ca_no+1
    cano.append(ca_no)
    f.write("Units : ")
    f.write(str(unit[v]))
    f.write("\n")
    a=uc(unit[v],hur)
    f.write("Bill Amount : ")
    f.write(str(a))
    f.write("\n")
    f.write("-"*42)
    print("-"*42)
    v=v+1
    
#Bill Printing

print("_"*42)
l=len(hn)
v=0
for i in range(l):
    today = datetime.date.today()
    new = datetime.date.today() + datetime.timedelta(20)
    print("Name :",hn[v].capitalize(),"     ","CA NO :",cano[v])
    print("Address :",hadd[v].capitalize())
    print("Meter Type :",mt[v])
    print("Contact No :", cn[v])
    print("Date of Bill",today)
    print("Due Date of Payment :",new)
    a=uc(unit[v],hur)
    print("Bill Amount :",a,"  ||  ","Units :",unit[v])
    if(a>=10000) : print("RED Bill , Please Pay on Time")
    ca_no=ca_no+2
    v=v+1
    print("-"*42)
    print("-> "*14)
    print("-"*42)
