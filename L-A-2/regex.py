import re as regex
# pattern="[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
# user_input=input()

# if(regex.search(pattern,user_input)):
#     print("Valid")
# else:
#     print("Invalid email")


# pattern="a(bc)*de"
# user_input=input()

# if(regex.search(pattern,user_input)):
#      print("Valid")
# else:
#      print("Invalid email")


Regexlst=[]
user_input=int(input("Enter Regex pattern list size "))
for i in range (user_input):
    if(i==0):
        Regexlst.append(input("Enter Regex "))
    else:
        Regexlst.append(input())
        
        
#print(Regexlst)
patternlst=[]

user_input=int(input("Enter pattern list size "))
for i in range (user_input):
    if(i==0):
        patternlst.append(input("Enter patterns "))
    else:
        patternlst.append(input())
count=0  
for i in range (len(patternlst)):
    for j in range(len(Regexlst)):
        if(regex.search(Regexlst[j],patternlst[i])):
            print(f'{"YES, "}{i+1}')
            print(Regexlst[j])
            print(patternlst[i])
            # patternlst.pop(j)
            # patternlst.insert(j,f'{"YES, "}{i+1}')
        elif(regex.search(Regexlst[j],patternlst[i])!=True and count<len(Regexlst)):
            count=count+1
        #      #print("Hello")
            if(count>=len(Regexlst)):
                print("NO, 0")
        