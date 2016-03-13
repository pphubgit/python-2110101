n=int(input())
data=[]
output=[]
kb=input().split()
first=False
last=False
mid=False
for i in range(n):
    data.append(int(kb[i]))
    output.append(0)
    print(data[i])
for i in range(0,n):
    if(i==0):
        first=True
    if(first==True):
        output[0]=(data[i]+data[i+1])/2
        first=False
    if(i==n-1):
        last=True
    if(last==True):
        output[n-1]=(data[n-2]+data[n-1])/2
        last=False
    else:
        output[i]=(data[i-1]+data[i]+data[i+1])/3
for i in range(0,n):
    print(int(output[i]))
