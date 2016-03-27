kb=input().strip()
inFile=open(kb,'r')
n=1;
a=0 #max
b=0 #min
for line in inFile:
    x,y=line.split()
    x=int(x);    y=int(y)
    if(n==1):
        a=x;          b=y
    if(n%2==1):
        if(a<=x):   a=x
        if(b>=y):   b=y
    if(n%2==0):
        if(a<=y):   a=y
        if(b>=x):  b=x
    n+=1
print(a,b)
