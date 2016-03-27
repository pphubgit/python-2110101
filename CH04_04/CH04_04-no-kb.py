kb = input().strip()
total=0
grade_list=[0,0,0,0,0,0]
inFile = open(kb,'r')
ok=False
for line in inFile:
    grade_list=line.split()
    if ok==False:
        n=int(grade_list[0])
        ok=True
    else:
        total=int(grade_list[1])+int(grade_list[2])+int(grade_list[3])+int(grade_list[4])+int(grade_list[5]) 
        if(total>=80):            grade='A'
        elif(total>=75):            grade='B+'
        elif(total>=70):            grade='B'
        elif(total>=65):            grade='C+'
        elif(total>=60):            grade='C'
        elif(total>=55):            grade='D+'
        elif(total>=50):            grade='D'
        else:            grade='F'
        print(grade_list[0]+' '+grade)
inFile.close()
