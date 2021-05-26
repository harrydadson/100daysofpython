# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter
from collections import Counter
a = 'aaaaaabbbbcccc'
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1))
print(my_counter.most_common(1)[0]) 
print(my_counter.most_common(1)[0][0]) 
print(list(my_counter.elements()))

# namedtuple
from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x, pt.y)

# OrderedDict
from collections import OrderedDict
ordr = OrderedDict()
ordr['a'] = 2
ordr['b'] = 3
ordr['c'] = 4
ordr['d'] = 6
print(ordr)

# defaultdict
from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['b'])

#deque
from collections import deque
d = deque()

d.append(1)
d.append(2)
d.appendleft(3)
d.extend([4,5,6])
print(d)





