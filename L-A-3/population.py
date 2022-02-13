# year=0 
# cp=1500
# population=cp
# while(cp<5000):
#     newArrive= cp*(5/100)
#     cp=cp+newArrive+100
#     year+=1
    
# print(year)

lst=[]
lst = [float(lst) for lst in input("Minimum And Maximum Value for the range of negative HP").split()]
cp=lst[0]
percentage=lst[1]
newpeople=lst[2]
maxrange=lst[3]
year=0
while(cp<maxrange):
    newArrive= cp*(percentage/100)
    cp=cp+newArrive+newpeople
    year+=1
    
print(year)