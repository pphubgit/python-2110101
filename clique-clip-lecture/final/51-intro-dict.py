'''Dict
มี key กับ Value
concept เหมือน dict จริง
'''
##s={key:value}
student1= {'name':'John',\
           'surname':'Smith',\
           'midterm':35,\
           'final':40,\
           1.5:'what'}
student1['name'] #--> John
student1[1.5]#--> what
## key และ value เป็น tuple ได้
## key เป็น list ไม่ได้ แต่ value เป็นได้
## สามารถเพิ่มข้อมูลใน dict ได้
a={}
a[2]=55
a['jack']='wooh'
print(a)
'''a={2:55,'jack':'wooh'}'''
##ข้อควรระวัง หาตัวที่ไม่มีใน dict -> error
