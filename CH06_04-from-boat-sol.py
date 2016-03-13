n=int(input())
num=[0]*n
mx_num=0
for i in range(n):
    num[i]=int(input())
num.sort()
f=1
max_freq=0
max_ans=num[0]
for i in range(1,n):
    if(num[i]==num[i-1]):
        f+=1
    else:
        f=1
    if(f>max_freq):
        max_freq=f
        max_ans=num[i]
print(max_ans)
