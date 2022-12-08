def isEven(i):
    return i>15==0
from functools import reduce
list1=[3,5,6,7,8,15,34]
output = list(filter(lambda i:i>15,list1))

print(output)

output2 = list(map(lambda i:i+2, list1))
output3 = reduce(lambda a,b:a+b,list1)
print(output3) 

output4 = reduce(lambda a,b:a/b,list1)