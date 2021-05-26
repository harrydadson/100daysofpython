# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

#product
from itertools import product
a = [1, 2]
b = [3,4]
prod = product(a,b)
print(list(prod))
print('--------')

#permutations
from itertools import permutations
a = [1,2,3]
perm = permutations(a,2)
print(list(perm))
print('--------')

# combinations
from itertools import combinations
a = [1,2,3,4]
comb = combinations(a, 2)
print(list(comb))
print('--------')

# accumulate
from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(list(acc))
print('--------')

#groupby
from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1,2,3,4]
group_obj = groupby(a, key=smaller_than_3)
for k, v in group_obj:
    print(k, list(v))

