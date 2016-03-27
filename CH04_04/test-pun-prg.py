name=input().strip()
infile=open(name,'r')
num_chk=False
for line in infile:
    if num_chk==False:
        num_chk=True
    else:
        ID,s1,s2,s3,s4,s5=[int(e) for e in line.split()]
        score=s1+s2+s3+s4+s5
        if 80<=score<=100:
            grade='A'
        elif 75<=score<=79:
            grade='B+'
        elif 70<=score<=74:
            grade='B'
        elif 65<=score<=69:
            grade='C+'
        elif 60<=score<=64:
            grade='C'
        elif 55<=score<=59:
            grade='D+'
        elif 50<=score<=54:
            grade='D'
        elif 0<=score<=49:
            grade='F'
        print(ID, grade)
infile.close()
        
