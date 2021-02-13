import random as ran
print("Brain Quiz Game")
print(" Choice Room","\n","1 Math Brain Game","\n","2 Math Quiz","\n","3 Science Quiz Game","\n","4 GK Quiz Game")
r=int(input("Enter Room No. :"))
qus=1
dict=0
hint=0
o=0
rp=0
rp1=0
rp2=0
rp3=0
hint1=0
hint2=0
o1=0
o2=0
for i in range(1):
  if(r==1):
   for i in range(1):
        q=["88,168,248,328,408,..","27,214,221,228,235","951,1951,950,1950,949,...","3,5,15,17,51,..","15,225,16,256,17,..."]
        qo=["440\n418\n488\n495","332\n237\n14\n242","1952\n1949\n1950\n1940","71\n55\n53\n55","337\n288\n289\n395"]
        h=["Table of 8","Table of 7","Big Addition","Plus Number of Times","Multiplie"]
        if(qus==1):
            print("Q.No",qus," ",q[0])
            print("_"*42)
            ans=input("")
            print("_"*42)
            if(ans==str("h") or ans==str("H")):
                print("Hint is ",h[0])
                ans=input()
                hint1=hint1+1
                print("_"*42)
            elif(ans=="o" or ans=="O"):
                print("Options Are ","\n"+qo[0])
                print("_"*42)
                ans=input()
                o1=o1+2
                print("_"*42)
        if(ans=="488"):
            rp=rp+5
        else:
           rp=rp+0
        qus=qus+1
        
        if(qus==2):
            print("Q.No",qus," ",q[1])
            print("_"*42)
            ans=input("")
            print("_"*42)
            if(ans=="h" or ans=="H"):
                print("Hint is ",h[1])
                ans=input()
                hint1=hint1+1
                print("_"*42)
            elif(ans=="o" or ans=="O"):
                print("Options Are ","\n",qo[1])
                print("_"*42)
                ans=input()
                o=o+2
                print("_"*42)
        if(ans=="242"):
            rp=rp+5
        else:
           rp=rp+0
        qus=qus+1
        if(qus==3):
            print("Q.No",qus," ",q[2])
            print("_"*42)
            ans=input("")
            print("_"*42)
            if(ans=="h" or ans=="H"):
                print("Hint is ",h[2])
                print("_"*42)
                ans=input()
                hint1=hin1t+1
                print("_"*42)
            elif(ans=="o" or ans=="O"):
                print("Options Are ","\n",qo[2])
                print("_"*42)
                ans=input()
                o1=o1+2
                print("_"*42)
        if(ans=="1949"):
            rp=rp+5
        else:
           rp=rp+0

        qus=qus+1
        
        if(qus==4):
            print("Q.No",qus," ",q[3])
            print("_"*42)
            ans=input("")
            print("_"*42)
            if(ans=="h" or ans=="H"):
                print("Hint is ",h[3])
                print("_"*42)
                ans=input()
                hint1=hint1+1
                print("_"*42)
            elif(ans=="o" or ans=="O"):
                print("Options Are","\n"+qo[3])
                print("_"*42)
                ans=input()
                o1=o1+2
                print("_"*42)
        if(ans=="55"):
            rp=rp+5
        else:
           rp=rp+0
        qus=qus+1
        
        if(qus==5):
            print("Q.No",qus," ",q[4])
            print("_"*42)
            ans=input("")
            print("_"*42)
            if(ans=="h" or ans=="H"):
                print("Hint is ",h[4])
                print("_"*42)
                ans=input()
                hint1=hint1+1
                print("_"*42)
            elif(ans=="o" or ans=="O"):
                print("Options Are ","\n",qo[4])
                print("_"*42)
                ans=input()
                o1=o1+2
                print("_"*42)
        if(ans=="289"):
            rp=rp+5
            
        else:
           rp=rp+0    
        ra=input("Do you want to play room Two also, Enter 2 :- ")
        if(ra=="2"):
            r=r+1
        else:
            break      
  if(r==2):
    print("_"*42)
    print("Welcome in Room Two || Math Quiz")
    qus=1
    rp1=0
    q0=ran.randint(3,3)
    q1=ran.randint(3,29)
    q2=ran.randint(3,9)
    q3=ran.randint(3,75)
    q4=ran.randint(3,9)
    q5=ran.randint(3,87)
    for i in range(5): 
        if(qus==1):
          if(q0==q1 and q2==q3 and q4==q5 and q4==q4 and q5==q5):
              continue
          elif(q0!=q1 and q2!=q3 and q4!=q5 and q0!=q1,q2,q3,q4,q5 and q1!=q0,q2,q3,q4,q5 and q2!=q1,q0,q3,q4,q5 and q3!=q1,q0,q2,q4,q5 and q4!=q1,q0,q3,q3,q5 and q5!=q1,q0,q3,q2,q4):
              print("Q.No",qus,(q0,q1,q0*q1,q2,q3,q2*q3,q4,q5))
              print("_"*42)
              ans=input("")
              print("_"*42)
              if(ans=="h" or ans=="H"):
                  print("Do Into")
                  print("_"*42)
                  ans=input("")
                  hint2=hint2+1
                  print("_"*42)
              elif(ans=="o" or ans=="O"):
                  print("Options are :- ","\n",(q4*q5)+10,"\n",(q4*q5)-6,"\n",(q4*q5)+23,"\n",(q4*q5))      
                  print("_"*42)
                  ans=input("")
                  o2=o2+2
        if(ans==str(q4*q5)):
            rp1=rp1+5
        else:
            rp1=rp1+0
            print("Right answer is :",q4*q5)
            print("_"*42)
        qus=qus+1
     
        if(qus==2):
          q0=ran.randint(3,3)
          q1=ran.randint(3,42)
          q2=ran.randint(3,9)
          q3=ran.randint(3,88)
          q4=ran.randint(3,9)
          q5=ran.randint(3,62)
          if(q0==q1 and q2==q3 and q4==q5 and q4==q4 and q5==q5):
              continue
          elif(q0!=q1 and q2!=q3 and q4!=q5 and q0!=q1,q2,q3,q4,q5 and q1!=q0,q2,q3,q4,q5 and q2!=q1,q0,q3,q4,q5 and q3!=q1,q0,q2,q4,q5 and q4!=q1,q0,q3,q3,q5 and q5!=q1,q0,q3,q2,q4):
              print("Q.No",qus,(q0,q4,(((q0+q4)+1000)),q2,q5,(((q2+q5)+1000)),q3,q1))
              print("_"*42)
              ans=input("")
              print("_"*42)
              if(ans=="h" or ans=="H"):
                  print("HINT IS : Do PLus and divide ans large number plus ")
                  print("_"*42)
                  ans=input("")
                  hint2=hint2+1
                  print("_"*42)
              elif(ans=="o" or ans=="O"):
                  print("Your Opions are")
                  print((int((q3+q1)+500)),"\n",(int(q3+q1)+600),"\n",(int((q3+q1))+1000),"\n",(int((q3+q1)+1120)))
                  print("_"*42)
                  ans=input("")
                  o2=o2+2
        if(ans==(str(q3+q1+1000))):
            rp1=rp1+1
        else:
            rp1=rp1+0
            print("Right Ans is :",(q3+q1)+1000)
            print("_"*42)
        qus=qus+1
        if(qus==3):
            q0=ran.randint(3,9)
            q1=ran.randint(3,23)
            q2=ran.randint(3,9)
            q3=ran.randint(3,65)
            q4=ran.randint(3,9)
            q5=ran.randint(3,99)
            if(q0==q1 and q2==q3 and q4==q5 and q4==q4 and q5==q5):
                continue
            elif(q0!=q1 and q2!=q3 and q4!=q5 and q0!=q1,q2,q3,q4,q5 and q1!=q0,q2,q3,q4,q5 and q2!=q1,q0,q3,q4,q5 and q3!=q1,q0,q2,q4,q5 and q4!=q1,q0,q3,q3,q5 and q5!=q1,q0,q3,q2,q4):
                print("Q No.",qus," Solve This.....","\n",q1,",",q0,",",int((q1+q0)*2),",",q2,",",q3,",",int((q2+q3)*2),",",q4,",",q5)
            print("_"*42)
            ans=input("")
            print("_"*42)
            if(ans=="h" or ans=="H"):
                print("Plus ans Multlipli")
                ans=input("")
                print("_"*42)
                hint2=hint2+1
            elif(ans=="o" or ans=="O"):
                print("Your Options are","\n"+(int(q4+q5+5)*2),"\n",(int(q4+q5)*2),"\n",(int(q4+q5+9)*2),"\n",(int(q4+q5+2)*2))
                ans=input()
                o2=o2+2
                print("_"*42)
        if(ans==str((q4+q5)*2)):
            rp1=rp1+5
        else:
            print("Wrong Answer , Right answer is ",((q4+q5)*2))
            print("_"*42)
            rp1=rp1+0
        qus=qus+1
       
        if(qus==4):
            q0=ran.randint(3,9)
            q1=ran.randint(3,99)
            q2=ran.randint(3,9)
            q3=ran.randint(3,55)
            q4=ran.randint(3,9)
            q5=ran.randint(3,87)
            if(q0==q1 and q2==q3 and q4==q5 and q4==q4 and q5==q5):
                continue
            elif(q0!=q1 and q2!=q3 and q4!=q5 and q0!=q1,q2,q3,q4,q5 and q1!=q0,q2,q3,q4,q5 and q2!=q1,q0,q3,q4,q5 and q3!=q1,q0,q2,q4,q5 and q4!=q1,q0,q3,q3,q5 and q5!=q1,q0,q3,q2,q4):
                print("Q.No",qus,"Solve This ","\n",q1,",",(str(q1*3)),",",q0,",",(str(q0*3)),",",q2,",",(str(q2*3)),",",q3,",",(str(q3*3)),",",q4,"...")
            print("_"*42)
            ans=input("")
            print("_"*42)
            if(ans=="o" or ans=="O"):
                print("Your Optinos are","\n",(q4*3+10),"\n",(q4*3),"\n",(q4*3+55),"\n",(q4*3-5))
                ans=input("")
                o2=o2+2
                print("_"*42)
            elif(ans=="h" or ans=="H"):
                print("Multipli pli Thrise")  
                ans=input()
                hint2=hint2+1
                print("_"*42)
        if(ans==str(q4*3)):
            	rp1=rp1+5
        else:
            print("Right Answer is ",(q4*3))
            print("_"*42)
            rp1=rp1+0
            
        qus=qus+1
        
        if(qus==5):
            q0=ran.randint(3,5)
            q1=ran.randint(3,9)
            q2=ran.randint(3,7)
            q3=ran.randint(3,9)
            q4=ran.randint(3,8)
            q5=ran.randint(3,9)
            if(q0==q1 and q2==q3 and q4==q5 and q4==q4 and q5==q5):
                continue
            elif(q0!=q1 and q2!=q3 and q4!=q5 and q0!=q1,q2,q3,q4,q5 and q1!=q0,q2,q3,q4,q5 and q2!=q1,q0,q3,q4,q5 and q3!=q1,q0,q2,q4,q5 and q4!=q1,q0,q3,q3,q5 and q5!=q1,q0,q3,q2,q4):
                print("Q.No.",qus,"Solve This ","\n",q0,",",q1,",",q1*q0,",",q2,",",q3,",",q2*q3,",",q4,",",q5,".....")
            print("_"*42)
            ans=input("")
            print("_"*42)
            if(ans=="o" or ans=="O"):
                print("Options are","\n",q4*q5,"\n",q4*q5+5,"\n",q4*q5+25,"\n",q4*q5+22)
                ans=input()
                o2=o2+2
                print("_"*42)
            elif(ans=="h" or ans=="H"):
                print("Into")
                print("_"*42)
                ans=input()
                hint2=hint2+1
        if(ans==str(q4*q5)):
            rp1=rp1+5
        else:
            rp1=rp1+0
            print("Wrong Answer , Right answer is ",q4*q5)
            print("_"*42)
        qus=qus+1
        ra=input("Do you want to play room Two als, Enter 3 :- ")
        if(ra=="3"):
            r=r+1
        else:
            break      
  if(r==3):
      gq=['Kideny stones are composed of \n........?','Waves which do not require any material medium for their propagations are .....?','What is the chemical name of chalk?','Which one of following does not Cantain silver?','Minamata disease is a nervous disorder caused by eating polluted fish by ....?']
      qpa=['A. Calcium Oxalate''\n''B. Pottasium Chloride''\n''C. Aluminium Nitrate''\n''D. Sodium Bicarbonate','A. Matter Waves''\n''B. Mechalical Waves''\n''C. Elastic Wavs''\n''D. Eleronmagnetic Waves','A. Calcium Sulphate''\n''B. Calcium Nitrate''\n''C. Calcium Phosphide''\n''D. Calcium Carbonate','A. German Silver''\n''B. Horn Silver''\n''C. Red Silver''\n''D. Lunar Silver','A. Mangnesium''\n''B. Lead''\n''C. Mercury''\n''D. Nickel']
      rans=['A','D','D','A','C']
      q=0
      ab=65
      print("Welcom In Room Three || Science Quiz Game")
      for i in range(5):         
         print("_"*42)
         print("QUS",chr(ab),"=",gq[q])
         print(qpa[q])
         print("_"*42)
         ua=input("Answer -> ")
         print("_"*42)
         answ=(ua.upper())
         if(answ==rans[q]):
             print("Right Answer")
             rp2=rp2+5
             
         else:
             print("Wrong Answer")
             rp2=rp2+0
         q=q+1
         ab=ab+1    
      print("_"*42)  
      ra=input("Do you want to play Room  Four also , Enter 4 :- ")
      if(ra=="4"):
          r=r+1
      else:
          break      
 
  if(r==4):
      gk=['Which Crop is shown in Large area''\n''in india','Galileo was an astronomer who ....','The words' " " 'smallest countre is ...?','What is the secound larges country''\n''(in size) in the world?','Which laguage is spoken in karnataka','The Currency notes are priented in ...']  
      gko=['A. Rice''\n''B. Wheat''\n''C. Sugercane''\n''D. Maize','A. Developed the telescope''\n''B. Discoverd four satellites of Juipter''\n''C. Discoverd The gravity Law''\n''D. All above','A. Canada''\n''B. Rissia''\n''C. Maldives''\n''D. Vactican City','A. Canada''\n''B. USA''\n''C. chaina''\n''D. Russia','A. Marathi''\n''B. Hindi''\n''C. Malayalam''\n''D. Kannada','A. New Delhi''\n''B. Nasik''\n''C. Nagpur''\n''D. Bombay']
      gka=['A','B','D','A','D']
      q=0
      qn=1
      print("Wlcome in General knowledge Questions Room")
      for i in range(5):
          print("_"*42)
          print("Qus",qn,"",gk[q])
          print(gko[q])
          print("_"*42)
          ua=input("Answer ->" )
          print("_"*42)
          answ=(ua.upper())
          if(answ==gka[q]):
              print("Right Answer")
              rp3=rp3+5
          else:
              print("Wrong Answer")
              rp3=rp3+0
          q=q+1
          qn=qn+1
          

print("_"*42)
tp=rp+rp1+rp2+rp3
print("Total Points ->",tp)
th=hint1+hint2
print("Total Hints Points are ->",th)
to=o1+o2
print("Options Points are ->",to)
Typ=tp-(th+to)
print("Your Total Points are :- ",Typ)
