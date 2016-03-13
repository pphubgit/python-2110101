bit=input()
n=0
for txt in bit:
    if(txt in '1'):
        n=n+1
if(n%2==0):
    bit=bit+'0'
else:
    bit=bit+'1'
print(bit)
