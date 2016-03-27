def repeat(s,n):
    k = ''
    for i in range(0,n):
        k += s #'''ไม่เปลี่ยนค่า
    s = k # ไม่ทำให้ตัวแปร s ในโปรแกรมหลัก เปลี่ยนไปด้วยหลังจากออกโปรแกรมย่อย
    return k
s_h = 'Hello'
print(repeat(s_h, 5))
print(s_h) # s_h ไม่ถูกเปลี่ยนเป็น k ด้วย ##ค่าจะเปลี่ยนเฉพาะในโปรแกรมย่อยแล้วจบ 
##เหมือนว่า s = s_h ; s = 'abc' ไม่จำเป็นว่า s_h ต้องเป็น abc ด้วย


#ตัวแปรไม่ไม่จำเป็นต้อง return ค่าเดียว
def fac(n):
    k = 1
    for i in range(1,n+1):
        k *= i
    return k
def list_fac(n):
    l = []
    for i in range(1,n+10):
        l.append()
    return l
####parameter เป็น list ได้
def sum_list(li):#li เป็น list
    sum = 0
    #li[0] = 0 '''เปลี่ยนได้ 
    for i in li:
        
        sum += i
    return sum

k = int(input())
li = list_fac(k)
print(li)# ออกมาทั้ง list ก็ได้ return เป็น list tuple ,etc ได้
print(sum_list(li))


