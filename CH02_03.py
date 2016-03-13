w=float(input())
h=float(input())
import math
body_surface=3.207*(10**-4)*(h**0.3)*(1000*w)**(0.7285-0.0188*(3+math.log10(w)))
print(body_surface)
