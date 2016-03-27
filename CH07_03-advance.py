#new(0) = 
#new(n+1)=new(n)-(a*(n)**2+b*(n)+c)/(2*a*(n)+b)
#new(n)=new(n-1)
def new(a,b,c,n,d):
    if abs(new(n+1)-new(n))<=d:return #new(0) = x_0
    return new(n)-(a*(n)**2+b*(n)+c)/(2*a*(n)+b)
