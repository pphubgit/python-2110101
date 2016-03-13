kb = input()
total=0
grade=''
a=''
b=''
n=0
total=0
grade_list=[0,0,0,0,0,0]
inFile = open(kb,'r')
for line in inFile:
    grade_list=line.split()
    if len(str(grade_list[0]))<10:
        n=int(grade_list[0])
    else:
    ##    print(b)
        total=int(grade_list[1])+int(grade_list[2])+int(grade_list[3])+int(grade_list[4])+int(grade_list[5]) 
        if(total>=80 and total<=100):
            grade='A'
        elif(total>=75):
            grade='B+'
        elif(total>=70):
            grade='B'
        elif(total>=65):
            grade='C+'
        elif(total>=60):
            grade='C'
        elif(total>=55):
            grade='D+'
        elif(total>=50):
            grade='D'
        elif(total<50):
            grade='F'
        print(grade_list[0]+' '+grade)
inFile.close()
