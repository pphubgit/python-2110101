n=int(input())
num=[0]*n
f=0
max_f=1
num[0]=int(input())
ans=0
for i in range(1,n):
    num[i]=int(input())
    if(num[i]==num[i-1]):
        f+=1
    elif(num[i]!=num[i-1]):
        f=1
    if()
