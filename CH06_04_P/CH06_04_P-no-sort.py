infile=open('score.txt','r')
ids=[]
ids_prnt=[]
n=0
for line in infile:
    line=line.split()
    ids.append(int(line[0]))
    n=n+1
for i in range(n):
    for j in range(n):
        if(ids[i]<=ids[j]):
            ids_prnt.append(ids[j])
for i in range(n):
    print(ids_prnt[i])
