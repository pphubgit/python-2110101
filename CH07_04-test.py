n=int(input().strip())
kb=[int(e)for e in input().split()]
for i in range(0,len(kb)):
    if i==0:print((kb[0]+kb[1])/2)
    elif (i==len(kb)-1):print((kb[len(kb)-2]+kb[i])/2)
    else:print((kb[i-1]+kb[i]+kb[i+1])/3)
