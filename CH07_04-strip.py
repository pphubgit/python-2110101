n=int(input().strip())
data=[]
output=[]
kb=input().split()
for i in range(n):
    data.append(int(kb[i]))
    output.append(0)
for i in range(0,n):
    if(i==0):
        output[0]=(data[i]+data[i+1])/2
    elif(i==n-1):
        output[n-1]=(data[n-2]+data[n-1])/2
    else:
        output[i]=(data[i-1]+data[i]+data[i+1])/3
for i in range(0,n):
    print(int(output[i]))
