#Dictionaries

d = {'Gaurav':888888, 'ram':459675, 'swati':458776}  #Here 'Gaurav' is Key and 888888 is Value

print(d['Gaurav']) #we can retrieve the value from string using it's Key

#Adding new Entry to Dicctionary
d['Sam'] = 78978
print(d) #added sam in dic

#In dictionaries Order Dosen't Matter

#Delete Entries from Dict
del d['Gaurav']
print(d) #'Gaurav' key and value is removed

#printing each element one by one
#WAY_1
for key in d:
    print("keys: ", key, " and Values: ", d[key])

#WAY_2
for k,v in d.items():
    print("key: ", k, "and value: ",v)

#Checking Keys in Dictionary
print('Sam' in d)
print('Gaurav' in d)

#For clearing dictionary we use d.clear()
print(d.clear())




# TUPLES : Tuples is slist of values grouped together
#Tuples is Heterogeneous i.e all of sits values have diffrent meanings
points = (5,8,9)
print(points[0])

address = ("khedkar nagar", "kOLA", 444116)
print(address)

#Tuples are immutable you cant change them




#EXERCISE
#Q.no 1
#1.1
population = {'china':143, 'india':136, 'USA':32, 'pakistan':21}
#1.2
#1.2.a
def check_ans(inp):
    if inp == 'Print':
        for k,v in population.items():
            print('k','==>',v)
    elif inp == 'add':
        inp1 = input()
        inp2 = int(input())
        if inp1 in population:
            print('Country already Exists')
        else:
            population[inp1] = inp2
        print(population)
    elif inp == 'remove':
        inp3 = input()
        if inp3 in population:
            del population[inp3]
            print(population)
        else:
            print('Country does not exists')
    elif inp == 'query':
        inp4 = input()
        print(population[inp4])

#TEST_ANS
check_1 = check_ans('remove')
check_2 = check_ans('add')

#Q.no 2
stocks = {'info':[600,630,620], 'ril':[1430,1490,1567],'mtl':[234,180,160]}

#2.1.a
def check_query(inp):
    if inp == 'print':
        for k,v in stocks.items():
            print(k,'==>',v)
    elif inp=='add':
        inp_ti = str(input())
        list_ti = []
        inp_pr = int(input())
        if inp_ti in stocks:
            print('stock already exists')
        else:
            list_ti.append(inp_pr)
            stocks[inp_ti] = list_ti
        print(stocks)

check_query(add)



