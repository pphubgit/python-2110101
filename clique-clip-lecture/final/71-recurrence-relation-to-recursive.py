#Recursive
# แก้ปัญหาเช่น
#sum(n) = 0+1+2+...+n
#sum(0) = 0 #base case
#sum(n) = n + sum(n-1) #คล้าย recurrence relation
def s(n):
    if n==0:return 0
    return n+ s(n-1)

print(s(5)) #--> 0+1+2+3+4+5

#fac fac(n)=1*2*...n
#fac(0) = 1
#fac(1) = 1
#fac(n) = n * fac(n-1)
#try me
def fac(n):
    if n ==0:return 1
    return n*fac(n-1)
#recurrsive จะเรียกตัวเองซ้ำ ใน def ที่ไหนก็ได้ แม้กระทั่ง return

print(fac(3))
