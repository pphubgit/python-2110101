def read_data():
     docs = {}
     n = int(input().strip())
     for i in range(n):
         tokens = input().strip().split()
         doc_name = tokens[0]
         doc_keywords = tokens[1:]
         for kword in doc_keywords:
             if kword in docs.keys():
                 docs[kword].add(doc_name)
             else:
                 docs[kword]={doc_name} #แปลว่า {keyword:doc_name , engineer:123.pdf}
     return docs
def search(docs,condition,search_keywords):
    if condition == 'and': 
        set_and=set();set_ans=set()##ให้คำตอบเป็น set_ans และ set_and คือค่า ที่รับมาแต่ละรอบ
        first_command=True
        for f in search_keywords:
            if first_command==True: #กำหนด set ในรอบแรกให้มีค่าขึ้นมาจากนั้นรอบถัดไปจะได้ข้าม if นี้
                set_and=set(docs[f])
                first_command=False
            else:
                set_ans=set_and.intersection(set(docs[f])) # นำค่าจากรอบแรกมา intersec กับรอบถัดไปเรื่อยๆ เพื่อหาตัวที่มีทุกค่า ถ้าสุดท้ายหมดก็ได้ set ว่าง
        return set_ans
    elif condition =='or':
        ans=set()
        for e in search_keywords:
            if e in docs.keys():
                ans.update(docs[e])
        return ans
    else:return list()

#==== Program starts here =======================
docs = read_data()
tokens = input().split()
print( sorted( search(docs, tokens[0], tokens[1:]) ) )
#=================================================
