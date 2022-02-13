s=input()
x="hello"
t=0
l=0
for item in range (len(s)):
    if(t<=4 and s[item]==x[t]):
         t=t+1
         l=l+1


                
if(l==5):
    print("YES")
else:
    print("NO")    