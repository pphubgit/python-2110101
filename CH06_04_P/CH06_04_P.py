file=open('score.txt')
ids=[]
n=0
for line in file:
    line=line.split()
    ids.append(line[0])
    n+=1
ids.sort()
for i in range(n):
    print(ids[i])
