txt,mix=input().split() #string
total=0
num='0123456789'
for i in mix: 
    if(i in num):
        total+=int(i)
print(txt[0].upper()+txt[1:].lower(),total)  # txt[0] = position 0 ->capital letter , txt[1:] position 1 to end lower character




##print(txt[0].upper()+txt[1:len(txt)].lower()+' '+str(total)) # position 0 = Capital letter
