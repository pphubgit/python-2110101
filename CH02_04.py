hr_in=int(input())
m_in=int(input())
hr_out=int(input())
m_out=int(input())
price=0
in_=hr_in*60+m_in
out_=hr_out*60+m_out
test=out_ - in_
if(test<=15):
    print(0)
elif(test>15 and test<=180):
    if(test%60==0):
        print(test//60*10)
    else:
        print(( (test//60)+1 )*10)
elif(test>180 and test<=360):
    if(test%60==0):
        print((( (test//60)-3)*20)+30)
    else:
        print(((( (test)//60)+1-3 )*20)+30)
else:
    print(200)
