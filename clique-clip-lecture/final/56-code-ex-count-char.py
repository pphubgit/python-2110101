s= 'abracadabra'
#c=1,a=5,b=2,d=1,r=2
count={}
#count['a'] -> 5
#count['c'] -> 1

for char in s:
    if char not in count:
        count[char] = 1
    else:
        count[char] +=1
print(count)
