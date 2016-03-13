##kb=input()
##kb=kb.split()
##mx=int(kb[0])
##for i in range(5):
##    if(int(kb[i])>=mx):
##        mx=int(kb[i])
##print(mx)


##kb=input()
##kb=kb.split()
##for i in range(5):
##    if(int(kb[i+1])>int(kb[i])):
##        mx=int(kb[i+1])
##print(mx)

kb=input()
a, b, c, d, e, f=kb.split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
f=int(f)
mx=max(a,b,c,d,e,f)
print(mx)
