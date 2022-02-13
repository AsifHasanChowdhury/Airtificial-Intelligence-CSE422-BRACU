x=int(input())
lst=[]
l=x
while (x>=1):

    if(l%x==0):
        res=l/x
        if(res>x):
            p=lst.count(res)
            if(p==0):
                lst.append(int(res))
        else:
            p=lst.count(x)
            if(p==0):
                lst.append(int(x))

    x=x-1

l=0

while(l<len(lst)):
    print(lst[l], end =" ")
    l=l+1

