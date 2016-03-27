def repeat(s,n):
    k = ''
    for i in range(0,n):
        k += s #'''ไม่เปลี่ยนค่า
    s = k

######ใช้ประกอบ แต่ def นี้ข้อนี้ไม่สน
def list_fac(n):
    l = []
    for i in range(1,n+1):
        l.append(fac(i))
    return l

def fac(n):
    k = 1
    for i in range(1,n+1):
        k *= i
    return k
#####
def sum_list(li):#li เป็น list
    sum = 0
    li[0] = 0 #'''เปลี่ยนได้ 
    for i in li:
        sum += i   #    list >I
    return sum     #          V
#เพราะว่า list เป็นจุดที่ชี้ไปที่ กล่อง  |_|_|_|_| ซึ่งไม่ได้เก็บที่ตัวมัน

#แต่ถ้า
def sum_list(li):#li เป็น list
    sum = 0
    for i in li:
        sum += i
    li = [] #'''ไม่เปลี่ยนค่า เพราะโยนทั้งตัวแปรแต่ไม่ได้ชี้ค่าในกล่อง --> กลายเป็นคิดเหมือน k เลย
    return sum

######
k = int(input())
li = list_fac(k)
#####
print(sum_list(li))
