#funcrion in python
def fac(n):
    k = 1
    for i in range(1,n+1):
        k *= i
    return k

##k = int(input())
##print(fac(k))

'''from 63 renovate to function'''

##list = input().split()
##n = int(list[0])
##k = int(list[1])
##print(fac(n)/fac(k)/fac(n-k))

''' ทำ combi เพิ่ม(n,k):'''
def combi(n,k):
    return fac(n)/fac(k)/fac(n-k)

def print_combi(n,k):
    print(combi(n,k))

list = input().split()
n = int(list[0])
k = int(list[1])


##print(combi(n,k))

print_combi(n,k)


#=========#EX 2
def repeat(s, n):
    k  = ''
    for i in range(0,n):
        k += s
    return k
print(repeat('Hello',5))
