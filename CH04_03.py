kb = input()
total=0
grade=''
a=''
b=''
total=0
inFile = open(kb,'r')
for line in inFile:
    a ,b ,c ,d ,e ,f=line.split()
##    print(b)
    total=int(b)+int(c)+int(d)+int(e)+int(f) 
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
    print(a+' '+grade)
inFile.close()
