import time
import random
time1=time.time()
#$#
st1=set()#blank set announce
def find_dup():#duplicate
    num=random.randrange(100,10000)#random integer from 100 to 999
    if(num not in st1):
        st1.add(num) #เหมือนกลับไปวน loop
        find_dup()
    if(num in st1):
        return num
print(find_dup())
#$#
time2=time.time()
print('Total calculate = ',time2-time1,' sec')
#$#
