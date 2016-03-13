n=int(input())
data=[]
f=[0]
mx=0
f=[0]*n # or append in loop for 
for i in range(n):
    kb=int(input())
    data.append(kb)
#    data.sort()
##    f.append(0)
for j in range(n):
    for k in range(n):
        if(data[j]==data[k]):
            f[j]=f[j]+1
##print('f',f)
##print('data',data)
##for i in range(n):
##    if(f[i]<f[i]):
##       mx=i
##print(data[i])
j=0 # max of i to compare
lst_max=[]#list of mode to compare
##lstPmax=[]#list_of_position+max
for i in range(n):
    for j in range(n):
        if(f[i]<f[j]):
##            lst_max[amnt]=data[j]
            lst_max.append(data[j])
##            amnt+=1
##            print('amnt =',amnt)
##            print('j =',j)
##print('amnt ',amnt)
lw=lst_max[0]
### find lower output in lw parameter
for i in range(n):
    for j in range(n):
        if(int(lst_max[i])<int(lw)):
            lw=lst_max[i]
##print('lst_max',lst_max)
print(lw)
