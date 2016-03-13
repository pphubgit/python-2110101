kb=int(input())
a=''
b=True
if(kb!=1):
    for i in range(kb,1,-1): # ถึง ก่อน 1 คือ 2
        print(i)
        if(kb%i==0):
            a=a+' '+i
        else:
            b=False
    else:
        break
if(b==True):
    print(a)
else:
    print('Prime Number')
