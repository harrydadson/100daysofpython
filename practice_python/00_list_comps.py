# Lists: ordered, mutable, allows duplicate elements

mylist = ['banana', 'cherry', 'apple']
print(mylist)

item = mylist[-2]
print(item)

for i in mylist:
    print(i)

if "banana" in mylist:
    print('yes')
else:
    print('no')

#append
mylist.append('lemon')
print(mylist)

# Remove
#items = mylist.remove('cherry')

# clear() - to delete everything

# sort() - to sort

# sorted()
mylist1 = [4, 3, 1, -1, -5, 10]
print(mylist1)

new_list = sorted(mylist1)
print(mylist1)
print(new_list)

#slicing
mylist2 = [1,2,3,4,5,6,7,8,9]
a = mylist2[::2]
print(a)

#copyin
list_org = ['banana', 'cherry', 'apple']

list_cpy = list_org.copy() # list(list_org) or list_org[:]

list_cpy.append('lemon')

print(list_cpy)
print(list_org)

#list comprehension

a = [1,2,3,4,5,6]
b = [i*i for i in a]

print(a)
print(b)

# first 10 perfect squares

squares = []
for i in range(10):
    squares.append(i * i)
print(squares)

# calculate the price after tax for a list of transactions

txns = [1.09, 23.56, 57.84, 4.56, 6.78]
Tax_rate = .08

def getPriceTax(txns):
    return txns * (1 + Tax_rate)

final_prices = map(getPriceTax,txns)
print(list(final_prices))

# filtering without using filter() but rather conditional

sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']

print(vowels)

# filtering consonants, with complex filter

def is_consonant(letter):
    vowels1 = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels1

consonants = [i for i in sentence if is_consonant(i)]
print(consonants)

# replace negative prices with 0 and leave the positive values unchanged

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]

print(prices)

# or using a function
def get_price(price):
    return price if price > 0 else 0
prices1  = [get_price(i) for i in original_prices]

print(prices1)