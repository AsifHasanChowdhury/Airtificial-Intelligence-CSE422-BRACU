x=input()
lst=[int(x) for x in input().split()]
res=0

for item in lst:
     res^=item
    
print(res)