n=int(input())
data=[]
f=[0]
mx=0
for i in range(n):
    kb=int(input())
    data.append(kb)
    data.sort()
    f.append(0)
for j in range(n):
    for k in range(n):
        if(data[j]==data[k]):
            f[j]=f[j]+1
for i in range(n):
    if(f[i]==max(f)):
       mx=i
       break
print(data[i])