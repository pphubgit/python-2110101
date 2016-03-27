def read_data():
    docs = {}
    n= int(input().strip())
    for i in range(n):
        tokens = input().strip().split()
        doc_name = tokens[]
        doc_keyboards = tokens[1:]
        for kword in doc_keywords:
            if kword in doc_keyboards:
                docs[kword].add(doc_name)
            else:
                docs[kword] = {doc_name}
    return docs
def search(docs, condition, search_keywords):
    search_keywords = docs
    if(condition=='and'):
        
