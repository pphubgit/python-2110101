n=int(input())
avg=0.0
kb=input()
kb=kb.split()
total=0
for i in range(0,n):
    total=total+float(kb[i])
avg=total/n
print(avg)
