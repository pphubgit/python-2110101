n=int(input().strip())
##data=[]
##output=[]
kb=input().split()
output=[0]*n
data=[0]*(n+2)
##for i in range(1,n-1):
j=0
i=1
for j in range(0,n):
    data[i]=int(kb[j])
    i+=1
for i in range(0,n):
    if(i==0):
        div=2
    elif(i==n-1):
        div=2
    else:
        div=3
##        output[n-1]=(data[n-2]+data[n-1])/2
    output[i]=(data[i]+data[i+1]+data[i+2])/div
for i in range(0,n):
    print(int(output[i]))
