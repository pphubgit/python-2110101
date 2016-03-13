kb=input().split()
n=int(kb[0])
r=int(kb[1])
s=int(kb[2])
import math
if(s==1):
    p=math.factorial(n)/(math.factorial(n-r))
    print(int(p))
if(s==2):
    c=math.factorial(n)/((math.factorial(n-r)*math.factorial(r)))
    print(int(c))
