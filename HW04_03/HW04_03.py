file=open(input())
result=[0,0,0,0,0]
for line in file:
    line=line.split()
    if (line[0].upper()=='BE'):
        result[0]=result[0]+1
    if (line[0].upper()=='SE'):
        result[1]=result[1]+1
    if (line[0].upper()=='VE'):
        result[2]=result[2]+1
    if (line[0].upper()=='ET'):
        result[3]=result[3]+1

result[4]=result[0]+result[1]+result[2]+result[3]
print(str(result[0])+' '+str(result[1])+' '+str(result[2])+' '+str(result[3])+' '+str(result[4]))
