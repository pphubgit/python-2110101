n=int(input())
data=[]
f=[0]
mx=0
f=[0]*n
for i in range(n):
    kb=int(input())
    data.append(kb)
for j in range(n):
    for k in range(n):
        if(data[j]==data[k]):
            f[j]=f[j]+1
j=0
lst_max=[]
for i in range(n):
    for j in range(n):
        if(f[i]<f[j]):
            lst_max.append(data[j])
lw=lst_max[0]
for i in range(n):
    for j in range(n):
        if(int(lst_max[i])<int(lw)):
            lw=lst_max[i]
print(lw)
