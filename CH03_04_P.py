total=int(input())
c=1
d=0
##while(c**2!=a**2+b**2):
##    c+=1
##    if(total!=a+b+c):
##        b+=1
##        if(total!=a+b+c):
##            a+=1
##print(c)

##=======
##for a in range (1,total):
##    if((a+b+c)==total and a**2+b**2==c**2):
##        break
##    else:
##        a+=1
##        if((a+b+c)==total and a**2+b**2==c**2):
##            break
##        else:
##            b+=1
##            if((a+b+c)==total and a**2+b**2==c**2):
##                break
##            else:
##                c+=1
##print(int(c))
##========

##for a in range (1,total):
##    for b in range(1,total):
##        if(a+b+((a**2+b**2)**0.5)==total):
##            print((a**2+b**2)**0.5)
##            print(int(c))

##for i in rangee(1,total):
##    if(a+b+c==total):
##        break

for a in range(1,total):
    for b in range(1,total):
        c=(a**2+b**2)**0.5
        if(a+b+c==total):
            d=c
print(int(d))
