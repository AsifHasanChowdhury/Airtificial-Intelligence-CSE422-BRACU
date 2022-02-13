import random as rd
lst=[]
lst2=[]
numberlst=[]
with open('F:\\CSE422\\New folder\\genetic.txt')  as file:
    lst=file.read().split()[1:]

for item in lst:
    if item=='l' :
        lst2.append('l')
        lst.remove(item)
    elif item=='d':
        lst2.append('d')
        lst.remove(item)
        

population=[]
population_size=2**len(lst2)-1
chromosome_length=len(lst2)

c=1
while c<=population_size:
    chrmosome=""
    for i in range(chromosome_length):
         gene=str(rd.randrange(0,2))
         chrmosome+=gene
    if chrmosome not in population:
        population.append(chrmosome)
        c=c+1
            
print(lst)
print(population)
print(len(population))






j=0
i=0
print(variationArray)
if(len(variationArray)%2==0):
    while i <(population_size-1):
        j=i+1
        if(j<population_size-1):
        #    print(f'{variationArray[i]}{" "}{variationArray[j]}' ,end=" ")
          value=rd.randrange(0, iterate)  
          temp=variationArray[i]
          p1=variationArray[i]
          p2=variationArray[j]
          p1=p1[:value]+p2[value:]
          variationArray[i]=p1
          p2=p2[:value]+temp[value:]
          variationArray[j]=p2
           
        i=j+1
#print(weight)
variationArray.sort()
print(variationArray)





import random as rd
lst=[]
lst2=[]
numberlst=[]
variationArray=[]
weight=[]


with open('F:\\CSE422\\New folder\\genetic.txt')  as file:
    lst=file.read().split()[1:]

def listAdjust():
    for item in lst:
        if item=='l' :
            lst2.append('l')
            lst.remove(item)
        elif item=='d':
            lst2.append('d')
            lst.remove(item)
    iterate=len(lst2)
    return iterate





def generate_popuation(iterate):
    population_size=2**len(lst2)-1
    
    check=1
    while check<=population_size:
        variation=""
        for j in range (iterate):
            variant=str(rd.randrange(0,2))
            variation+=variant
        if variation not in variationArray:
            variationArray.append(variation)
            check=check+1
            
            
    variationArray.sort()
    variationArray.pop(0)
    
    return population_size

 
def FitnessGeneration():
    for i in variationArray:
        weightv=0
        iterator=0
        for j in i:
            if(j=='1') and (lst2[iterator]=='l'): 
                weightv=weightv-int(lst[iterator])
            
            elif (j=='1') and (lst2[iterator]=='d'):
                weightv=weightv+int(lst[iterator])
                
            iterator+=1
        # if(weightv==0):
        #     print(i)
        weight.append(weightv)
  
#CROSSOVER
#print(population_size)
#print(variationArray[125])

#print(value)
def crossover(iterate,population_size):
    j=0
    i=0
    print(variationArray)
    if(len(variationArray)%2==0):
        while i <(population_size-1):
            j=i+1
            if(j<population_size-1):
            #   print(f'{variationArray[i]}{" "}{variationArray[j]}' ,end=" ")
                value=rd.randrange(0, iterate)  
                temp=variationArray[i]
                p1=variationArray[i]
                p2=variationArray[j]
                p1=p1[:value]+p2[value:]
                variationArray[i]=p1
                p2=p2[:value]+temp[value:]
                variationArray[j]=p2
            
            i=j+1
#print(weight)
#variationArray.sort()
#print(variationArray)



#Mutation
def Mutation(iterate):
    bit_flip=rd.randrange(0, iterate)  

    print(f'{"bit_flip "}{bit_flip}')

    for item in variationArray:
        if(item[bit_flip]=='0'):
            item[bit_flip].replace(item[bit_flip],'1')
        else:
            item[bit_flip].replace(item[bit_flip],'0')
    print("After Mutation")
    print(variationArray)


x=listAdjust()
population_size=generate_popuation(x)
FitnessGeneration()
crossover(x,population_size)
Mutation(x)




print(f'{"pre p1 " }{variationArray[0]}')
print(f'{"pre p2 " }{variationArray[1]}')
temp=variationArray[0]
p1=variationArray[0]
p2=variationArray[1]
p1=p1[:value]+p2[value:]
variationArray[0]=p1
p2=p2[:value]+temp[value:]
variationArray[1]=p2

print(f'{"new p1 " }{variationArray[0]}')
print(f'{"new p2 " }{variationArray[1]}')