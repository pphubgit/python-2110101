n=int(input())
a=[]; b=[]
for i in range(n):
    a.append(int(input()))
a.sort()
for i in range(n-1,-1,-1): #(3,0,-1) ได้ 3 2 1 ไม่เอา 0 (ได้ stop+1)-> ก่อน stop
    print(a[i])
