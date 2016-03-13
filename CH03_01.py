kb=0
n=0
txt=''
bmi_list=[]
while(kb!='-1'):
        kb=input()
        if(kb=='-1'):
            break
        txt=kb.split()
        bmi_list = bmi_list+['']
        w=int(txt[0])
        h=int(txt[1])
        bmi_list[n]=w/((h/100)**2)
        n=n+1
for i in range(n):
    print(bmi_list[i])
