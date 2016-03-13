kb=input().split()
n=int(kb[0])
sub=int(kb[1])
q=sub
##p=['']*n
output=[]
ttl=0
for i in range(n):
        pp=input().split()
         # ต้องเริ่มใช้ ช่อง 1 ไม่ใช่ 0
        
        for j in range(sub):
            #n=q
            if(pp[j]=='X'):
                pp[j]=0
                q=q-1
            if(pp[j]=='A'):
                pp[j]=4
            if(pp[j]=='B+'):
                pp[j]=3.5
            if(pp[j]=='B'):
                pp[j]=3
            if(pp[j]=='C+'):
                pp[j]=2.5
            if(pp[j]=='C'):
                pp[j]=2
            if(pp[j]=='D+'):
                pp[j]=1.5
            if(pp[j]=='D'):
                pp[j]=1
            if(pp[j]=='F'):
                pp[j]=0
            ttl=ttl+pp[j]
        output.append(ttl/q)
        q=sub
        ttl=0
for k in range(0,len(output)):
##    output[k]=round(output[k],2)
##    print('output',output[k])
    print('%.2f' %output[k])   
