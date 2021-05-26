# Tuple: ordered, immutable, allows duplicate elements

mytuple = ('Max', 28, 'Boston') # tuple with one element
print(mytuple)

for x in mytuple:
    print(x)

if "Max" in mytuple:
    print('yes')
else:
    print('no')

my_tuple = ('a', 'p', 'p', 'l','e')
print(my_tuple.count('p'))

print(my_tuple.index('l'))

# slicing

a = (list(range(11)))
print(a)

b = a[::-1]
print(b)

# tuple unpacking

mytuple1 = ('Max', 28, 'Boston')

name, age, city = mytuple1

print(name)
print(age)
print(city)

mytuple2 = (0,1,2,3,4)
i1, *i2, i3 = mytuple2

print(i1)
print(i3)
print(i2)