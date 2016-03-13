file   = open("score.txt")
ids    = []
grades = []
for line in file:
    tokens = line.split()
    ids.append(tokens[0])
    grades.append(tokens[1])
file.close()
#---------  อ่านเสร็จแล้วค่อยค้น -----------
found  = False
key_id=''
show=[]
i=0
n=0
while(key_id !='-1'):
    found  = False
    key_id = input()
    show.append('')
    for index in range(len(ids)):
        if (key_id == ids[index]):
            found = True
            break
        ##ใช้ range len เพราะว่ายังไงเราก็เอาไม่เกิน index แล้ว index ก็ไม่เกิน len(ids)
    if (found):
        show[i]=grades[index]
    else:
        show[i]='No'
    i=i+1
    n+=1
del show[n-1]
for i in range(n-1):
    if(show[i]=='No'):
        print('Not found')
    else:
        print(show[i])
