import random as rd
def crossover(iterate,population_size):
    variationArray=['0000000','1111111','1010101']
    j=0
    i=0
    print(f'{"Variation len"}{len(variationArray)}')
    if(len(variationArray)%2==0):
        print("WOK")
        while i <=(population_size-1):
            j=i+1
            if(j<=population_size-1):
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
            
    
    
    elif(len(variationArray)%2!=0):
        print("WWOK")
        while i <=(population_size-1):
            j=i+1
            
            if(i==(population_size-1)):
                print("WWOK")
                j=i-1
                value=rd.randrange(0, iterate)  
                print(f'{"Randrange "}{value}')
                temp=variationArray[i]
                p1=variationArray[i]
                p2=variationArray[j]
                p1=p1[:value]+p2[value:]
                variationArray[i]=p1
                p2=p2[:value]+temp[value:]
                variationArray[j]=p2
                break
            
            elif(j<=population_size-1):
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
    print(variationArray)        

crossover(7,3)