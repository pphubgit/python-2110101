def an(n):
    f=1
    if n==0:
        f=1
        return f
    if n>=1:
        for i in range(1,n+1):
            f=f*i
        return f
kb=int(input())
print(an(kb))
