data=[1,2,3,5,9,21,30]
to_find = int(input())
found=False
for element in data:
    if to_find == element:
        found = True
        break
if found:
    print('FOUNDED')
else:
    print('NOT FOUNDED')
