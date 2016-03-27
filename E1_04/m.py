kb=input().strip()
infile=open(kb,'r')
idx=[]
t1=[]
t2=[]
t3=[]
total=0
n=0
chk=[]
blank=True
al=False
for line in infile:
    test=line.split()
    if((int(test[1]) and int(test[2]) and int(test[3]))>0):
        idx.append(test[0])
        total=int(test[1])+int(test[2])+int(test[3])
        t1.append(total)
        t2.append(total*1.5)
        t3.append('[]')
        chk.append(1)
    else:
        tmpt3=''
        if(test[1]=='0'):
            tmpt3+='#1'
        if(test[2]=='0'):
            tmpt3+='#2'
        idx.append(test[0])
        total=int(test[1])+int(test[2])+int(test[3])
        t1.append(total)
        t2.append(total*1.5)
        tmpt3='['+tmpt3+']'
        t3.append(tmpt3)
        chk.append(0)
    n+=1
    blank=False
for i in range(n):
##    if(al==True):

    print(idx[i],t1[i],t2[i],t3[i])
if(blank==True):
    print('No data!')
elif(0 not in chk):
    print('All students submit homeworks.')