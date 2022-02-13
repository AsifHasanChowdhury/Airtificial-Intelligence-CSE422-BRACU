f=open ("F:\\CSE422\\bfs.txt","r")
for i in f:
   line_space_remove=i.strip()
   split_line=line_space_remove.split()
   print(split_line[1])