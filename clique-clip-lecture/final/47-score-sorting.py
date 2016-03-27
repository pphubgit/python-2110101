infile = open('47score.txt','r')
stnt_id = []
grade = []
#Bubble sort
for line in infile:
    x = line.split()
    x[0] = int(x[0])
    x[1] = float(x[1])
    stnt_id.append(x[0])
    grade.append(x[1])

for i in range(len(grade)):
    for j in range(len(grade)-1):
        if grade[j]< grade[j+1]: #น้อยไปมาก
            grade[j],grade[j+1]=grade[j+1],grade[j]
            stnt_id[j],stnt_id[j+1]=stnt_id[j+1],stnt_id[j]
for i in range(len(grade)):
    print('Student ID:',stnt_id[i],' GPA = ',grade[i])
