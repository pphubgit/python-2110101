infile = open('45score.txt','r')
id_to_find = int(input())

for line in infile:
    x = line.split()
    if id_to_find ==int(x[0]):
        found = True
        print('Student ID:',x[0],' Grade =',x[1])

if not found:
    print('Not Found')

#การทำ sequence search in python มักเป็น for each
