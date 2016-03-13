kb=input()
kb=kb.split('/')
month=['JAN','FEB','MAR','APR','MAY','JUN'\
       ,'JUL','AUG','SEP','OCT','NOV','DEC']
print(kb[1]+' '+month[int(kb[0])-1]+' '+kb[2])
