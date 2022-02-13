import numpy as dp
import queue
#x=input("Enter vertex Number")
#x=int(x)
q=queue.Queue()
#print(arr_zeros)
#arr_zeros[1,2]=100
#print(arr_zeros[1,2])



#f=open ("F:\\CSE422\\bfs.txt","r")
vertex=0
edge=0
line=0
count=0

#with open('F:\\CSE422\\bfs.txt') as file:
#    for line in file:
#        print(line.rstrip())
#        vertex=line
#        Edge=line
#        break
       
arr_zeros=dp.zeros((vertex,vertex),dtype=int)

f=open ("F:\\CSE422\\bfs.txt","r")
for i in f:
   line_space_remove=i.strip()
   split_line=line_space_remove.split()
   #print("hello",i)
   if(count==0):
    vertex=int(split_line[0])
    count=count+1
    #print(split_line[0])
   elif(count==1):
    edge=int(split_line[0])
    arr_zeros = dp.zeros((vertex,vertex),dtype=int)
    count=count+1
    #print(split_line[0])
   elif(count>1):
    #print("Asche")
    bi_directional_edge_1=int(split_line[0])
    bi_directional_edge_2=int(split_line[1])
    
    arr_zeros[bi_directional_edge_1,bi_directional_edge_2]=int(1)
    arr_zeros[bi_directional_edge_2,bi_directional_edge_1]=int(1)
    #print(split_line[1])
  #lst.append(split_line)
  
print(arr_zeros)
discover=dp.zeros((1,vertex),dtype=int)
visited=dp.zeros((1,vertex),dtype=int)
q.put(0)
while not q.empty():
  u=q.get()
  v=0
  while(v<vertex):
    if(arr_zeros[u,v]==1 and visited[0,v]==0):
      q.put(int(v))
      visited[0,v]=1
      discover[0,v]=discover[0,u]+1
    v=v+1
print(f'{"Nora distance from 6 is "}{discover[0,0]}{" hop"}')

