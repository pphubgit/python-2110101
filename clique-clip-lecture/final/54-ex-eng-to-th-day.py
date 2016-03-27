'''
mon -> จันทร์
tue -> อังคาร
'''
en2th = {'MON':'จันทร์'\
         'TUE':'อังคาร'\
         'WED':'พุธ'\
         'THU':'พฤหัส'\
         'FRI':'ศุกร์'\
         'SAT':'เสาร์'\
         'SUN':'อาทิตย์'}
#a[key]--> value
s = input('Day =')
if s.upper() in en2th:
    print(en2th[s.upper()])
else:
    print('Invalid Input')
