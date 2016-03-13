a=0
total=0
b=-1
# รอบแรกโปรแกรมวิ่งเปล่าๆ ไป ดังนั้น b=-1
i=0
while(i!=-1):
    b=b+1
    total=total+i
    i=float(input())
if(b!=0):
    print(total/b)
else:
    print('No Data')
