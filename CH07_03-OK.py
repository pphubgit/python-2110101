def newton(a,b,c,x_n,d,n):
    x_n_1=x_n-(a*(x_n)**2+b*(x_n)+c)/(2*a*(x_n)+b)
    if(abs(x_n_1-x_n)<=d):
        print(n)
        return 0
        #ทำไม return n ได้ none
    else:
        k=x_n_1
        n+=1
        newton(a,b,c,k,d,n)


'''
'''
##def newton(a,b,c,x_n,d):
##    x_n_1=x_n-(a*(x_n)**2+b*(x_n)+c)/(2*a*(x_n)+b)
##    if(x_n_1-x_n>d):
##        k=x_n_1
##        n+=1
##        newton(a,b,c,k,d)
##    else:return n
kb=[float(e) for e in input().split()]
newton(kb[0],kb[1],kb[2],kb[3],kb[4],1)#รับค่า 0 เป็น การกำหนด n=1 แทน
