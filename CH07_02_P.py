kb=input().split()
sm=int(input())
n=0
i=0
while(i!=len(kb)-1):
    for j in range(i+1,len(kb)):
        if( (int(kb[i])+int(kb[j]))==sm):
            n+=1
        if(j==len(kb)-1):
            i+=1
print(n)
