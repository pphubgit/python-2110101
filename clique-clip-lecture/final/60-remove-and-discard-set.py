#ลบข้อมูลใน set
#remove and discard set
set.remove(value)
ลบค่า value ใน set ถ้าไม่มี จะ error
set.discard(value)
ลบค่า value ใน set ไม่มี ไม่เป็นไร
s={1,2,3,4,5}
s.remove(2)
s-->{1,3,4,5}
s.discard(3)
s-->{1,4,5}
s.add('d')
s-->{1,'d',4,5}
s.remove(2)--> error 2 not found
