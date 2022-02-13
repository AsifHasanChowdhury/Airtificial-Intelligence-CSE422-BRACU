x=input()
lst=[int(x) for x in input().split()]
res=0

n=len(lst)
sum=int((n*(n+1))/2)
print(sum)
mainsum=0
for item in lst:
    mainsum+=item
print(mainsum)
