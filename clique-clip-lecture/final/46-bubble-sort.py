#Bubble sort
data= [3,4,1,12,17,0,-1,2]

for i in range(len(data)):
    for j in range(len(data)-1):
        if data[j]>data[j+1]:
            data[j],data[j]=data[j+1],data[j]
print(data)
