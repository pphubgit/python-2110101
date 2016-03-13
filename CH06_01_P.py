##n=int(input())
##num=['']
##for i in range(0,n):
##    num = num+['']
##for k in range(0,n):
##    kb = input()
##    num[k]=int(kb)
##for j in range(0,n-1):
##    if num[j]<num[j+1]:
##        num[j],num[j+1] = num[j+1],num[j]
##for l in range(0,n):
##    print(num[l])


## append เพิ่มข้อความใน list
##n=int(input())
##num = []
##for i in range(0,n):
##    kb=int(input())
##    num.append(kb)
##for j in range(0,n-1):
##    if num[j]<num[j+1]:
##        num[j],num[j+1] = num[j+1],num[j]
##for l in range(0,n):
##    print(num[l])


num=[]
for i in range(0,n):
    kb=int(input())
    num.append(kb)
for j in range(1,n-1):
    if num[j]<num[j+1]:
        num[j],num[j+1] = num[j+1],num[j]
for l in range(1,n):
    print(num[l])
