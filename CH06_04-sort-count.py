n=int(input())
num=[0]*n
f=[0]*n
for i in range(n):
    num[i]=int(input())
num.sort()
for i in range(n):
    f[i]=num.count(num[i])
for i in range(n):
    if(f[i]==max(f)):
        print(num[i])
        break
