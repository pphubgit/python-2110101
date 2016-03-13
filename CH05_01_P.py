kb=input()
obj='0123456789'
txt=''
for i in obj:
    if(i not in kb):
        txt=txt+i+' '
if (txt==''):
    print('No missing digits')
else:
    print(txt.strip())
