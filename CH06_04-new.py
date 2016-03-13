n=int(input())
num=[0]*n
for i in range(n):
    num[i]=int(input())
f=[0]*n
for i in range(n):
    for j in range(i):
        if(num[i]==num[j]):
            f[i]+=1
tmp=max(num)
for k in range(n):
    if(f[k]==max(f)):
        if(num[k]<tmp):
            tmp=num[k]        
print(tmp)
