#key value item in python
s.keys() #--> คืน list ของ key ออกมา
s.values()#--> list ของ values ออกมา
s.items() #--> list ของ [(key,value),(key2,value2)] ออกมา

#ประโยชน์
for key in s.keys(): # ถ้าไม่ได้ใส่ เป็น for a in s เหมือน for a in s.keys()
    print(key)
for (k,v) in s.items():
    print('key=',k,'value=',v)
