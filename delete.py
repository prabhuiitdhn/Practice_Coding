# later understand setdefault, defaultdict, and dict comprehensions, counters
# also from collections

from collections import OrderedDict

# OrderedDict example
od = OrderedDict()
od["name"] = "Alice"
od["age"] = 25
od["city"] = "NYC"
print(od)  # OrderedDict([('name', 'Alice'), ('age', 25), ('city', 'NYC')])

# Iteration respects insertion order
for key, value in od.items():
    print(key, value)


from collections import OrderedDict

# OrderedDict example
nod = OrderedDict()
nod["name"] = "Alice"
nod["age"] = 25
nod["city"] = "NYC"
print(nod)  # OrderedDict([('name', 'Alice'), ('age', 25), ('city', 'NYC')])

# Iteration respects insertion order
for key, value in nod.items():
    print(key, value)

