import random as r
import math
student_id=input(" Enter your Student ID ")
lst = [int(lst) for lst in input("Minimum And Maximum Value for the range of negative HP ").split()]
maxv=lst[0]
minv=lst[1]
depth=int(student_id[0])*2
turns=depth
branch=int(student_id[2:3])
life=student_id[-2:][::-1]
#print(f'{"Initial Life "}{life}')

total_leaf=int(depth)**int(branch)+1
leaf_list=[]
visited_list=[]
for i in range(total_leaf):
    
 leaf_list.append(r.randrange(maxv,minv))
 
leaf_list=[]
leaf_list=[19,22,9,2,26,16,16,27,16]

def AlphabetaPruning(alpha,beta,branch, depth, maxplayer,position):
    if(depth==0):
        cal=position
        visited_list.append(cal)
     #   print(f'{ "branch "}{branch }{" maxc "}{maxc}{" minc "}{minc}{" Cal "}{cal}')
        return leaf_list[cal]
    
    if(maxplayer==True):
        maxEval= -(math.inf)
        for maxc in range (branch):
            maxplayer=False
            eval=AlphabetaPruning(alpha,beta,branch,depth-1,maxplayer,position*branch+maxc)
            maxEval=max(maxEval,eval)
            alpha=max(alpha,maxEval)
            if(alpha>=beta):
                break
        return maxEval
    else:
        minEval=math.inf
        for minc in range (branch):
            maxplayer=True
            eval=AlphabetaPruning(alpha,beta,branch,depth-1,maxplayer,position*branch+minc)
            minEval=min(minEval,eval)
            beta=min(beta,eval)
            if(alpha>=beta):
                break
        return minEval
          
value=AlphabetaPruning(-math.inf,math.inf,branch, depth,True,0)


print(f'{"Depth and branches ratio is "}{depth}{":"}{branch}')
print(f'{"Terminal States (leaf node values) are "}{leaf_list}')
print(
    f'{"Left life (HP) of the defender After maximum damage caused by the Attacker is "}{int(life)-int(value)}')
print(f'{"After Alpha-beta Pruning Leaf Node Comparisons "}{len(leaf_list)-len(visited_list)}')
print(visited_list)