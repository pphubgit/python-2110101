n=int(input())
counts={}
num=[0]*n
for i in range(n):
    num[i]=int(input())
num=tuple(num)
for j in num:
    if j in counts:
        counts[j]+=1
    else:
        counts[j]=1
anss=max(num)
##p=0
for m in counts.keys():
    if(max(counts.values())==counts[m]):
        if(m<anss):
            anss=m
##    else:
##        anss
print(anss)
##    print(m)
    
##for 
##    if(max(ii)):
##        if(max)
##        print(num[i])
##        break
