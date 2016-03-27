#LIst of tuple
books=[('book1','123xx',256,20),\
       ('python','000xx',141,99),\
       ('physic','12222x',100,22)]
print(books)#--> ได้ list of tuple
for each_tuple in books:
       print(each_tuple[0])#--> ได้ book1 python physic

'''============'''
for (title,isbn,price,amount) in books: #math กับ tuple จำนวน เท่ากัน(ในวงเล็บ 4 ตัว)
    print(title,price,amount)
'''ได้
book1 256 20
python 141 99
physic 100 22
'''
