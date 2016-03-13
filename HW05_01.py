n=int(input())
lst_data=[]
total=0
counts={}

for i in range(n):
    x=int(input())
    lst_data.append(x)
    total+=x
lst_data.sort()
##counts=tuple(lst_data)
for x in lst_data:
    if x in counts:
        counts[x]+=1
    else:
        counts[x]=1
mean=total/n
if n%2!=0:
    p=int((n+1)/2)
    med=lst_data[p-1]
else:# จำวนวนกับ ช่องต้อง ลบ 1
    p=int(n/2)
    q=int((n/2)+1)
    med=(lst_data[p-1]+lst_data[q-1])/2
for i in counts:
    if(counts[i]==max(counts.values())):
        mode=i
        break
print(mean,med,mode)
