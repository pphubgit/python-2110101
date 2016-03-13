import math
a, k ,m=input().split()
a=int(a)
k=int(k)
m=int(m)
n=0
if(k==0):
    n=1
elif(k%2==0):
    n=(a**(math.floor(k/2)))**2%m
elif(k%2==1):
    n=a*(a**(math.floor(k/2)))**2%m
print(n)
