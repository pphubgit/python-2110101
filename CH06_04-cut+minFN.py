n=int(input())
data=[]
lst_max=[]#list of mode to compare
f=[]
for i in range(n):
    kb=int(input())
    data.append(kb)
    f.append(0)
for i in range(n):
    for j in range(n):
        if(data[i]==data[j]):
            f[i]=f[j]+1
for i in range(n):
    for j in range(n):
        if(f[i]<f[j]):
            lst_max.append(data[j])
lw=min(lst_max)
print(lw)
