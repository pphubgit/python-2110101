kb=0
n=0
find=[]
i=0
found = False
while(kb!='-1'):
    kb=input()
    find.append(kb)
    find[n]=kb
    n=n+1
file=open('score.txt','r')
for line in file:
    line=line.split()
    i_d = line[0]
    grade = line[1]
    for i in range(n):
        if(i_d == find[i]):
            print(grade)
        else:
            print('Not Found')

