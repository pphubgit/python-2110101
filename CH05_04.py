n=int(input())
num=['']
for i in range(0,n):
    num = num+['']
for k in range(0,n):
    kb = input()
    num[k]=int(kb)
for j in range(0,n-1):
    if num[j]<num[j+1]:
        num[j],num[j+1] = num[j+1],num[j]
for l in range(0,n):
    print(num[l])
