##kb=input()
##n=0
##for txt in kb:
##    if(txt in ' '):
##        continue
##    if(txt in kb.upper().strip()):
##        n+=1
##print(n)


kb=input()
n=0
for txt in kb:
    if(txt.isupper()):
       n+=1
print(n)
