n=int(input())
output=''
for i in range(2,n):
    if(n%i==0):
        output=str(i)+' '+output
if(output==''):
    output='Prime Number'
print(output)
