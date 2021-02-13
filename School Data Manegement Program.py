"""Its Progam Use all Functions of List and other"""
print("        Indian Students School")
print("DATA MANAGEMENT SERVER")
C11=["PAWAN","Vineet","ASHU","ANSUL","ANUBHAV","Arya"]
C12=["VINAY","RAJIVE","RIYA","POOJA"]
print("Roll NO :","Name : ")
for i in C11 and range(len(C11)):
    print(" ",i," "*5,C11[i])
print("Enter M for Check marks")
n=int(input("enter roll no :"))
m=[[25,63,52],[39,52,59],[52,64,54],[56,61,88],[65,26,45],[55,45,36]]
s=["Hindi","English","Math"]
print("NAME : ",f'{C11[n]}')
for i in range(3):
    print(f'{s[i]:12}:{m[n][i]:5}',end="   ")
    if(m[n][i]>=33):
        print("PASS")
    else:
        print("Fail")
print("Maximam","    :",f'{max(m[n]):4}')
print("TOTAL MARKS :",f'{sum(m[n]):5}')
