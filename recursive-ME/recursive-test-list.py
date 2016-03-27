import time
import random
time3=time.time()
#$#
st=[]#blank set announce
def find_dup():#duplicate
    num=random.randrange(100,10000)#random integer from 100 to 999
    if(num not in st):
        st.append(num) #เหมือนกลับไปวน loop
        find_dup()
    if(num in st):
        return num
print(find_dup())
#$#
time4=time.time()
print('Total calculate = ',time4-time3,' sec')
#$#


time1=time.time()
#$#
st1=set()#blank set announce
def find_dup():#duplicate
    num1=random.randrange(100,10000)#random integer from 100 to 999
    if(num1 not in st1):
        st1.add(num1) #เหมือนกลับไปวน loop
        find_dup()
    if(num1 in st1):
        return num1
print(find_dup())
#$#
time2=time.time()
print('Total calculate = ',time2-time1,' sec')
#$#
