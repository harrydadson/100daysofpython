# sets: unordered, mutable, no duplicates

myset = set()

myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4)

myset.remove(4)
print(myset)

#looping

for x in myset:
    print(x)

# union

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

#inteersection
i = odds.intersection(primes)
print(i)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)
print(diff)

diff1 = setB.difference(setA)
print(diff1)

diff2 = setB.symmetric_difference(setA)
print(diff2)

print(setA.update(setB))


print(setA.intersection_update(setB))

# set comprehension

quote = 'life, uh, finds a way'
unique_vowels = {i for i in quote if i in 'aeiou'}
print(unique_vowels)




