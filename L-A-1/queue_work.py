
import numpy as dp
import queue
q=queue.Queue()
array_from_file = dp.loadtxt("F:\\CSE422\\New folder\\work2.txt", dtype=dp.chararray)
count=1
#print(array_from_file)
vertex_lst=[]    
row=array_from_file.shape[0]
col=array_from_file.shape[1]
matrix=array_from_file

print(matrix)
lst=[]
itemindex = dp.where(array_from_file=='A')
lst.append(itemindex)
print(itemindex[0])
x=int(len(lst[0]))

print(x)
