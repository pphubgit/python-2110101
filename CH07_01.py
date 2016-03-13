kb=input().split()
n=int(kb[0])
sort=int(kb[1])
num=[]
for i in range(n):
    kb=int(input())
    num.append(kb)
if sort==0:
    num.sort(key=None, reverse=False) #low-> hi
else:
    num.sort(key=None, reverse=True)
for i in range(n):
    print(num[i])
