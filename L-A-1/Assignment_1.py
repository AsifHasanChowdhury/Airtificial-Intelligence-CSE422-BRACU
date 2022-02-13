
import numpy as dp
import queue
stack = queue.LifoQueue()


array_from_file = dp.loadtxt("F:\\CSE422\\New folder\\work.txt", dtype=dp.chararray)

#print(array_from_file)
vertex_lst=[]    
row=array_from_file.shape[0]
col=array_from_file.shape[1]
matrix=array_from_file

print(matrix)

def flood_fill_dfs(x,y):
   land=1
   stack.put((x,y))
   while not stack.empty():
       
     tuple=stack.get()
 #    print(tuple)
     u=tuple[0]
     v=tuple[1]
     array_from_file[u,v]='N'     
     right=v+1
     left=v-1
     up=u-1
     down=u+1
     lst=[[u,right],[u,left],[up,v],[down,v],[up,right],[up,left],[down,right],[down,left]]
     
     i=0
     while(i<len(lst)):
            x=lst[i]
            if(x[0]>=0 and x[0]<row) and (x[1]>=0 and x[1]<col):
        
                if(matrix[x[0],x[1]]=='Y'):
                  matrix[x[0],x[1]]='N'
                  stack.put((x[0],x[1]))
                  land=land+1
              
            i=i+1
                 
   return land    


def graph():
    for i in range (row):
        for j in range (col):
            if(array_from_file[i,j]=='Y'):
                x= flood_fill_dfs(i,j)
                vertex_lst.append(x)
    

graph()
print(vertex_lst)
