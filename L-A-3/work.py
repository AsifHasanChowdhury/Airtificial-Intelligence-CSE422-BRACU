import math
import random as r
#leaf_list=[19,22,9,2,26,16,16,27,16]
leaf_list=[18,13,5,12,10,5,13,7,17,8,6,8,5,11,13,18]
# lst.remove(1)
# print(lst)
leaf_visited=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
depth=4
branch=2


def AlphabetaPruning(alpha,beta,branch, depth, maxplayer,position):
    count=0
    if(depth==0):
        # print(f'{" branch "}{branch}{" fc "}{fc}{" Childs "}{childs}')
        cal=position
        leaf_visited[cal]=1
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


print(AlphabetaPruning(-math.inf,math.inf,branch,depth,True,0))
#print(len(leaf_list))
#print(count)
print(leaf_visited)