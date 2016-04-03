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
    ans={}
    tmp=[]
    for a in search_keywords:
        for i in doc[a]
##    return ans
    if condition=='and'
    
##    elif condition=='or':
##    else:return list()

#==== Program starts here =======================
docs = read_data()
tokens = input().split()
print( sorted( search(docs, tokens[0], tokens[1:]) ) )
#=================================================
