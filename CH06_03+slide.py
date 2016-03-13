key_id=''
not_found = True
grade_table=['']
n=0
while(key_id!='-1'):
    key_id = input()
    file = open('score.txt')
    for line in file:
        tokens = line.split()
        i_d     = tokens[0]
        grade  = tokens[1]
        if (key_id == i_d):
            grade_table[n]=grade
            grade_table=grade_table+['']
        else:
            grade_table[n]='False'
            grade_table=grade_table+['']
##        else:
##            note_found = False
##    if(not_found == False):
##        print('Not Found')
    file.close()
    n+=1

for i in range(n-1):
    if(grade_table=='False'):
        print('Not Found')
    else:
        print(grade_table[i])
