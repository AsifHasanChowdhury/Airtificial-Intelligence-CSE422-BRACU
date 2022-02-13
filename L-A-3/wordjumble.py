Regexlst=[]
user_input=int(input())
for i in range (user_input):
        Regexlst.append(input())
        
        
x=input()
count=0
backup=""
for item in Regexlst:
  if(item in x):
    count=count+1
    backup+=item
#print(count)
s=set(backup)
l=set(x)
#print(len(s))
#print(len(l))
if(len(l)==len(s) and count==len(Regexlst)):
  print("Yes")
else:
  print("No")
