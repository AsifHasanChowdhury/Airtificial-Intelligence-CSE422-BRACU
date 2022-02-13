# Python3 program to demonstrate the
# use of replace() method
import random as rd
string = ['1000001','1101111']
bit_flip=rd.randrange(0, 7)  
#print(bit_flip)
hold=string[0]
# print(hold)
#print(hold[bit_flip])
# hold=hold[:bit_flip]+'1'+hold[bit_flip+1:]
# print(hold)

i=0
while(i<len(string)):
    l=string[i]
    if(l[bit_flip]=='1'):
        l=l[:bit_flip]+'0'+l[bit_flip+1:]
        string[i]=l
    elif(l[bit_flip]=='0'):
        l=l[:bit_flip]+'1'+l[bit_flip+1:]
        string[i]=l
    i=i+1
print(string)
# for item in string:
#     if (item[bit_flip]==0):
#           print(f'{"This is before Mutation "}{item}')
#           item=item[:bit_flip]+'0'+item[bit_flip+1:]
#           print(f'{"This is After Mutation "}{item}')
#     else:
#          print(f'{"This is before Mutation "}{item}')
#          item=item[:bit_flip]+'1'+item[bit_flip+1:]
#          print(f'{"This is After Mutation "}{item}')





#