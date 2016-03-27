'''function ในทาง programming
มองเป็นโรงงาน มี input --> function --> output
function ไม่จำเป็นต้องมีตัวแปรเดียวก็ได้
input --> str list , etc
output--> str list ,mix , etc ไม่มีก็ได้

EX.'''
list = input().split()
n = int(list[0])
k = int(list[1])
nfac = 1
for i in range(1,n+1):
    nfac *=i
kfac = 1
for i in range(1,k+1):
    kfac *=i
nmkfac = 1
for i in range(1,n-k+1):
    nmkfac *= i
print(nfac/kfac/nmkfac)
#code มีความซ้ำซ้อน
# ถ้ามี function code จะสั้นลง
## แก้ไข ส่วนที่ error ได้ง่าย
### code อ่านง่ายขึ้น
#### ใช้ recursive ได้
