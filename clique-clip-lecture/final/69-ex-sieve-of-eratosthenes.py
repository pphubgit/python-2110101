
#เร็วกว่านี้อีก sieve of eratosthenes
#1 not prime
#2 is prime -> 4,6,8,... not prime
#3 is prime (ยังไม่เคยถูกเอาออก) -> 6,9,12,...
#4 เอาออกไปแล้ว
#5 is prime (ยังไม่เคยถูกเอาออก)
def list_prime_seive(n):
    p_list=[]
    s = set([i for i in range(2,n+1)])  #set มี remove
    while(len(s) > 0):
        top = s.pop()
        p_list.append(top)
        for k in range(top*2,n+1,top):#ตัวแรกที่คิดคือ 2 เท่าของ top อย่าง 2 เป็นจำนวนเฉพาะก็ remove 4 ขึ้นไป
            if k in s:s.remove(k)# ระวัง 2 remove 6 และ 3 ก็ remove 6 เลยต้อง if
    return p_list
print(list_prime_seive(k))
