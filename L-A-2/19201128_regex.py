import re as regex
Regexlst=[]
user_input=int(input("Enter Regex pattern list size "))
for i in range (user_input):
    if(i==0):
        Regexlst.append(input("Enter Regex "))
    else:
        Regexlst.append(input())
        
        
patternlst=[]

user_input=int(input("Enter pattern list size "))
for i in range (user_input):
    if(i==0):
        patternlst.append(input("Enter patterns "))
    else:
        patternlst.append(input())

for i in range (len(patternlst)):
    for j in range(len(Regexlst)):
        if(regex.search(Regexlst[j],patternlst[i])):
            print(f'{"YES, "}{j+1}')
            break
        elif(regex.search(Regexlst[j],patternlst[i])!=True and j==len(Regexlst)-1):
            print("NO, 0")
            break
        