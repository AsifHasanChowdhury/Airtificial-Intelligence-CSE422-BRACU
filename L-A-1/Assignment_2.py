
import numpy as dp
import queue
q=queue.Queue()
hc=0
array_from_file = dp.loadtxt("F:\\CSE422\\New folder\\work2.txt", dtype=dp.chararray,skiprows= 2)
count=0
print(array_from_file)
#count=count-1
vertex_lst=[]    
row=array_from_file.shape[0]
col=array_from_file.shape[1]
matrix=array_from_file
#print(matrix)


def bfs(q):
    
    while not q.empty():
        
        tuple=q.get()
        u=tuple[0]
        v=tuple[1]
        right=v+1
        left=v-1
        up=u-1
        down=u+1
        array_from_file[u,v]='T'
        lst=[[u,right],[u,left],[up,v],[down,v]]

        i=0
        while(i<len(lst)):
            x=lst[i]
            if(x[0]>=0 and x[0]<row) and (x[1]>=0 and x[1]<col):
        
                if(matrix[x[0],x[1]]=='H'):
                  matrix[x[0],x[1]]='A'

            i=i+1
                 
        
def graph():
    for i in range (row):
        for j in range (col):
            if(array_from_file[i,j]=='A'):
                q.put((i,j))
               
    bfs(q)
                
    
def checkHuman():

    t=0
    for i in range (row):
        for j in range (col):
            if(matrix[i,j]=='A'):
             t=t+1
            
    return t

x=checkHuman()
while q.empty() and x>0:
        graph()
        count=count+1
        x=checkHuman()
        
print(array_from_file)

print(count-1)
