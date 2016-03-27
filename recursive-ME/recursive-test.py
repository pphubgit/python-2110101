#From internet
#ให้สุ่มจำนวน 3 หลักขึ่นมาโดยจะหยุดสุ่มเมื่อซ้ำจำนวนเดิม แล้วให้แสดงค่าที่ซ้ำออกมา
#normal process
'''
1.สุ่มตัวเลข
2.เอาเลขที่สุ่ม ไปค้นใน set
3.เช็คว่าซ้ำหรือไม่ ถ้าซ้ำ ให้น้ำค่านี้ไปใช้ ถ้าไม่ซ้ำ ให้ สุ่มเลขใหม่อีกครั้ง
4.เอาเลขที่สุ่มได้จากข้อ 4 ที่อยู่ในเงื่อนซ้ำกับของเดิม ไปเช็คกับ database
5.ทำซ้ำข้อ 3 (จะหยุดเมื่อเลขซ้ำใน set)
6.ทำซ้ำข้อ 4
7.ทำซ้ำข้อ 3 (จะหยุดเมื่อเลขซ้ำใน set)
8.ทำซ้ำข้อ 4
.....
'''
#normal program
import random
#calculate speed program ในบรรทัด #$#
#$#
import time
time1=time.time()
#$#
st1=set()
ans=0
while True:
    num1=random.randrange(100,1000)#random integer from 100 to 999
    if num1 not in st1:
        st1.add(num1)
    if num1 in st1:
        ans=num1
        break
print(ans)
#$#
time2=time.time()
print('Total calculate = ',time2-time1,' sec')
#$#

#recursive process
'''
สุ่มตัวเลข
เอาตัวเลขที่สุ่ม ไปค้นใน set
เช็คว่าซ้ำหรือไม่ ถ้าซ้ำ ให้นำค่านี้ไปใช้ และหยุดการทำงานชุดคำสั่งข้อ 1-2 ถ้าไม่ซ้ำ(return) ให้เริ่มทำข้อ 1 ใหม่
'''
##import random
#$#
time3=time.time()
#$#
st=set()#blank set announce
def find_dup():#duplicate
    num=random.randrange(100,1000)#random integer from 100 to 999
    if(num not in st):
        st.add(num) #เหมือนกลับไปวน loop
        find_dup()
    if(num in st):
        return num
print(find_dup())
#$#
time4=time.time()
print('Total calculate = ',time4-time3,' sec')
#$#
#### ทำเพื่อพิสูจน์มห้เห็นว่า recursive เร็วกว่า
