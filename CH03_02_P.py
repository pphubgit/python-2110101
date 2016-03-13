n=int(input())
total=0
if(n!=0):
    for i in range(n):
        a=float(input())
        total=total+a
    total=total/n
    print(total)
else:
    print('No Data')
