# Dictionary: Key-Value pairs, Unordered, Mutable

mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

value = mydict['name']
print(value)

mydict['email'] = 'hd@xmail.com'
print(mydict)

#deleting del , pop(), popitem()
#del mydict['name']
#print(mydict)

# checking

if 'name' in mydict:
    print(mydict['name'])

# or

try:
    print(mydict['name'])
except:
    print('error')

# looping

for key in mydict: # or mydict.keys()
    print(key)

# or

for k, v in mydict.items():
    print(k,v)

# copy a dict
mydict_cpy = mydict.copy()
mydict_cpy1 = dict(mydict)

# dictionary comprehension
squares = {i: i*i for i in range(10)}
print(squares)
