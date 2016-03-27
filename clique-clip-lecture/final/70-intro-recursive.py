#Recursive
#แก้ปัญหาซ้ำซ้อน
#tower of hanoi 3 tower เอาแผ่นใหญ่ย้ายไป tower 3 ล่างสุดก่อน
#start tower=1 des tower=3 temp tower =2 
def move(s,start,des):
    if s==1:
        print('move plate size',s,'form',start,'to',des)
        return
    temp = 6 - start - des 
    move(s-1,start,temp)# ข้างบนเล็กกว่า 1 ขั้น  เก็บที่อื่นก่อน
    print('move plate size',s,'form',start,'to',des)
    move(s-1,temp,des)# move temp to des
move(3,1,3)
#ref:https://www.mathisfun.com/games/towerofhanoi.html

#recursive คือ function ที่เรียกใช้งานตัวเอง
