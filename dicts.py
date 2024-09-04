a = {
    'name':'Naresh',
    'surname':'Baraili',
    'age': 30,
    'gender': 'Male'
    }
print(a['name'])
print(a['surname'])

aa = {
    'name':'Naresh',
    'surname':'Baraili',
    'age': 30,
    'gender': 'Male',
    'address':['Gorkha','Kathmandu']
    }
print(aa['address'][-1])

#get all keys from dict
print(aa.keys())
#get all values from dict
print(aa.values())
#to get number of keys and values
print(len(aa))
#sends key error
# print(aa['middle_name'])
#puts the value to '-' if key is not found
print(aa.get('middle_name','-'))

#add key and value in dict(replaces the value if the key exists if not creates new key value pair)
aa['religion']='Atheist'
aa['address']='Gorkha'
print(aa)

test = {
    'name':'Broadway',
    'company':'test',
    'number':{
        'type':'NTC',
        'mobile':9843747501
    }
}
print(test['number']['type'])
print(test.keys())
print(test.values())


test = {
    'name':'Broadway',
    'company':'test',
    'number':[
        {
        'type':'NTC',
        'mobile':9843747501
    },
    {
        'type':'Ncell',
        'mobile':9813445685
    }
    ]
}
print(test['number'][0]['type'])
print(test['number'][1]['type'])

test.update({'name':'Naresh','number':1,'test':'testing'})
print(test)

#deletes elements by keys
del test['number']
print(test)

#deletes entire dict variable
del test
# print(test)


#remove using pop
test = {
    'name':'Broadway',
    'company':'test',
    'number':123
}
tt=test.pop('number')
print(test)
print(tt)

#removes the last element but is not recommended usually in programming
test.popitem()
print(test)

#clear(makes the test variable empty but doesnot delete the variable)
test.clear()
print(test)

#Exercise
name = input('Enter your name: ')
address = input('Enter your address: ')
number = int(input('Enter your number: '))
gender = name = input('Enter your gender: ')
sts = name = input('Enter your marietal status: ')


a = {
    'name':name,
    'address':address,
    'number':number,
    'gender':gender,
    'Marietal Status':sts

}
print('Your input is successfully added to dictionary')
print(a)

#alternative method
x = {}
x['name']=input('Enter your name: ')
x['address']=input('Enter your surname: ')
x['number']=int(input('Enter your contact number: '))
x['gender']=(input('Enter your age: '))
x['sts']=input('Enter your marietal status: ')
print('Your input is successfully added to dictionary')
print(x)
