inFile=open('score.txt','r')
student=[0,0]
s_id=0
grade=0
kb_id=input()
for line in inFile:
    line = line.split()
    s_id = line[0]
    grade = line[1]
    if (kb_id == s_id):
        break
print(grade)
inFile.close()
