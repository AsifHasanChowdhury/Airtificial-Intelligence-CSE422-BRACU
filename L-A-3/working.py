import math
import random as r
student_id="17301106"
depth=int(student_id[0])*2
turns=depth
branch=int(student_id[2:3])
life=student_id[-2:][::-1]
print(f'{"Initial Life "}{life}')
# print(branch)
print(f'{"Depth and branches ratio is "}{depth}{":"}{branch}')
count=0
total_leaf=int(depth)**int(branch)+1
#print(total_leaf)

leaf_list=[]

for i in range(total_leaf):
    
 leaf_list.append(r.randrange(1,21))


print(leaf_list)
def AlphabetaPruning(alpha,beta,branch, depth, maxplayer,maxc,minc,count):
    if(depth==0):
        # print(f'{" branch "}{branch}{" fc "}{fc}{" Childs "}{childs}')
        maxc=int(maxc)
        minc=int(minc)
        cal=(branch*maxc)+minc
        #print(cal)
     #   print(f'{ "branch "}{branch }{" maxc "}{maxc}{" minc "}{minc}{" Cal "}{cal}')
        return leaf_list[cal]
    
    if(maxplayer==True):
        maxEval= -(math.inf)
        for maxc in range (branch):
            maxplayer=False
            eval=AlphabetaPruning(alpha,beta,branch,depth-1,maxplayer,maxc,minc,count)
            maxEval=max(maxEval,eval)
            alpha=max(alpha,maxEval)
            if(alpha>=beta):
                count=count+1
                break
        return maxEval
    else:
        minEval=math.inf
        for minc in range (branch):
            maxplayer=True
            eval=AlphabetaPruning(alpha,beta,branch,depth-1,maxplayer,maxc,minc,count)
            minEval=min(minEval,eval)
            beta=min(beta,eval)
            if(alpha>=beta):
                count=count+1
                break
        return minEval


solve=AlphabetaPruning(-math.inf,math.inf,branch,depth,True,0,0,count)
print(
    f'{"Left life (HP) of the defender After maximum damage caused by the Attacker is "}{int(life)-int(solve)}')

print(f'{"After Alpha-beta Pruning Leaf Node Comparisons "}{len(leaf_list)-count}')