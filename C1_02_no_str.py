a=int(input())
b=int(input())
c=int(input())
d=int(input())
if(a<b):
    a,b=b,a
    if(1<=c<=20 and 3<=d<=23):
        b,d=d,b
    else:
        a,c=c,a
else:
    if(a%2==0 and (b+d)%2==1 or c%10==0):
        a+=1
        b=b+d
        c=2*c
    elif((c%100)//10==1):
        a=b+c+d
    elif( ((c%100)//10)%2 ==0):
        b=a+c-d
    else:
        c=b-d+a
s=1
while( ((a+c)//(b+d))>0 ):
    if( ((a+c)//(b+d))<=0):
        break
    s=s+b+a+d*c
    b=b+5
    a=a-7
print(s)
