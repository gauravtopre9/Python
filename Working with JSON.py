#JSON : JAVA SCRIPT OBJECT NOTATION

book = {}
book['tom'] ={
    'name':'tom',
    'add' :'mumbai',
    'phone': 7744
}
book['bob'] = {
    'name':'bob',
    'add':'pune',
    'phone': 9881
}

import json

a = json.dumps(book) #converting to JSON FORMAT
print(a) #Printing JSON
with open("C://Users//GAURAV//Desktop//Machine Learning//Python_learn//json.txt","w") as f: #Writing json to txt
    f.write(a)

f = open("C://Users//GAURAV//Desktop//Machine Learning//Python_learn//json.txt","r") #Reading Json File
s = f.read()
print(s)

books = json.loads(s) # converting JSON to Dict
print(books)
print(type(books))
print(books['tom'])
print(books['tom']['phone'])

for person in books:
    print(books[person])
    

