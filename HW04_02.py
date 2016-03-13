kb=input().split()
txt=kb[0]
mix=kb[1]
total=0
num='0123456789'
for i in range(len(mix)):
    if(mix[i] in num):
        total+=int(mix[i])
print(txt[0].upper()+txt[1:len(txt)].lower()+' '+str(total))
