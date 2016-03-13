txt=input().split()
total=0
n=0
for i in range(len(txt)):
    if(int(txt[i])<0):
        break
    total=int(txt[i])+total
    n+=1
print(total/n)
