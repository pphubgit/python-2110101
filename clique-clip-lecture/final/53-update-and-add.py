k={'a':1,'b':2,'c':3}
l={'a':2,'d':4}
k.update(l) #--> {'b': 2, 'c': 3, 'a': 2, 'd': 4}
k.pop('b') #--> pop=ลบออก ใช้กับ keys และมันคืนค่าออกมาให้ด้วยว่า value ที่ถูกลบตาม key นั้นคืออะไร
#pop ค่าที่ไม่มี ลบไม่ได้
'a' in k #--> true แต่หาแบบ binary search
#in จะค้นหา key เท่านั้น 
