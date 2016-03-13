f_kb=input()
a, b=f_kb.split()
a=int(a)
data=[]
n=0
for i in range(a):
    kb=input()
    data.append(kb)
    if(data[i]==b):
        n+=1
print(n)
