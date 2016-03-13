vowels='aeiou'
alphabet='bcdfghjklmnpqrstvwxyz'
txt=input().lower()
vw=0
aph=0
for i in txt:
    if(i in vowels):
        vw+=1
    if(i in alphabet):
        aph+=1
print(str(vw)+' '+str(aph))
