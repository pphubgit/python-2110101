#67 
#ให้เลขมาหาว่าเป็นจำนวนเฉพาะหรือไม่
'''def is_prime(n):#ใช้ได้แต่ยังไม่เร็วพอ
    for i in range(2,n):
        if n%i==0:
            return False
        return True
'''
#ทำให้เร็วขึ้น คิดการแยกตัวประกอบแบบ 2 ตัว ตัวมากที่สุดที่เป็นค่าน้อยจะเป็น sqrt ของค่านั้น เช่น 100=10*10

##accelerate
def is_prime(n):#ใช้ได้แต่ยังไม่เร็วพอ
    limit = int(math.sqrt(n))+1
    for i in range(2,limit+1):
        if n%i==0:
            return False
        return True


k = int(input())
print(is_prime(k))
