#แก้ bug # ลืม 1 กับlimit 2 ยังใช้ไม่ได้
def is_prime(n):#ใช้ได้แต่ยังไม่เร็วพอ
    if n==1: return False #return จะไม่ทำข้างล่างแล้ว
    limit = int(math.sqrt(n))+1
    for i in range(2,limit+1):
        if n%i==0 and n!=i :#กรณี n=i ก็ได้เศษ 0 แต่อาจไม่ใช่จำนวนเฉพาะก็ด้
            return False
        return True


k = int(input())
print(is_prime(k))
#ถ้าให้ 1-10 ถามตัวไหนเป็น prime บ้าง
def list_prime(n):
    p_list = []
    for i in range(1,n+1):
        if is_prime(i):p_list.append(i)
    return p_list
print(list_prime(k))

#เร็วกว่านี้อีก sieve of eratosthenes
#1 not prime
#2 is prime -> 4,6,8,... not prime
#3 is prime (ยังไม่เคยถูกเอาออก) -> 6,9,12,...
#4 เอาออกไปแล้ว
#5 is prime (ยังไม่เคยถูกเอาออก)
