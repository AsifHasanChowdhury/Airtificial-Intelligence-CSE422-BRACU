
import numpy as dp
import queue
q=queue.Queue()
array_from_file = dp.loadtxt("F:\\CSE422\\New folder\\work.txt", dtype=dp.chararray)


vertex_lst=[]    
row=array_from_file.shape[0]
col=array_from_file.shape[1]
matrix=array_from_file

def flood_fill_bfs(x,y):
   land=0
   q.put((x,y))
   while not q.empty():
     tuple=q.get()
     u=tuple[0]
     v=tuple[1]
     
     if(array_from_file[u,v]=='Y'):
         q.put((u,v))
         array_from_file[u,v]=='N'
         land=land+1
         
         lst=[[u,v+1],[u,v-1],[u-1,v],[u-1,v+1],[u-1,v-1],[u+1,v+1],[u+1,v+1],[u+1,v-1]]
         if(u-1>0 and u+1<array_from_file.shape[0] and v-1>0 and v+1<array_from_file.shape[1]):
             for i in lst:
                 if(matrix[lst[i]]=='Y'):
                     q.put(lst[i])
                     array_from_file[u,v]=='N'
                     land=land+1
                     print(land)
   return land    

for i in range (row):
    for j in range (col):
         if(array_from_file[i,j]=='Y'):
            print("Work")
            x= flood_fill_bfs(i,j)
           
            vertex_lst.append(x)

print(vertex_lst)
            
print(array_from_file)

         
         