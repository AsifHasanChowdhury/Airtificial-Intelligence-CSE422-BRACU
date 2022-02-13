S="Hello"

for i in range(len(S)):
  j=0
  count=0
  while(j<len(S)):
     if(S[i]== S[j] and i!=j):
          count=count+1
     j=j+1

  if(count==0):
    print(S[i])
    break