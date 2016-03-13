kb=input().split()
sm=int(input())
n=0
for i in range(len(kb)):
    for j in range(i):
        if( (int(kb[i])+int(kb[j]))==sm):
            n+=1
print(n)
