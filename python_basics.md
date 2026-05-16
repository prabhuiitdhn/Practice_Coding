# Python Basics - Interview Revision Guide

---

## 1. Data Types & Mutability

### Mutable vs Immutable

| Mutable (can change in-place) | Immutable (cannot change) |
|-------------------------------|---------------------------|
| list | int |
| dict | float |
| set | str |
| bytearray | tuple |
| | frozenset |
| | bool |
| | bytes |

```python
# Immutable — creates a new object
x = 10
x = x + 1  # new object, id(x) changes

# Mutable — modifies in-place
lst = [1, 2, 3]
lst.append(4)  # same object, id(lst) stays same
```

**Interview Tip:** When you pass a mutable object to a function, changes inside the function affect the original. Immutable objects don't get affected.

---

## 2. Python Built-in Data Structures

### Lists (Dynamic Arrays)
```python
lst = [1, 2, 3, 4, 5]

# Operations & Time Complexity
lst.append(6)       # O(1) amortized
lst.pop()           # O(1) — from end
lst.pop(0)          # O(n) — from front (shift all)
lst.insert(0, 99)   # O(n)
lst[2]              # O(1) — index access
lst.remove(3)       # O(n) — search + shift
len(lst)            # O(1)
x in lst            # O(n) — linear search
lst.sort()          # O(n log n) — Timsort
lst.reverse()       # O(n)
```

### Tuples (Immutable Lists)
```python
t = (1, 2, 3)
# Faster than lists, hashable (can be dict keys)
# Use when data shouldn't change
t[0]          # O(1)
len(t)        # O(1)
x in t        # O(n)
```

### Sets (Hash-based, Unordered, Unique)
```python
s = {1, 2, 3, 4}

s.add(5)            # O(1) average
s.remove(3)         # O(1) average
s.discard(99)       # O(1), no error if missing
x in s              # O(1) — THIS IS WHY SETS ARE POWERFUL
s1 | s2             # union O(len(s1)+len(s2))
s1 & s2             # intersection O(min(len(s1),len(s2)))
s1 - s2             # difference O(len(s1))
```

### Dictionaries (Hash Maps)
```python
d = {"name": "Alice", "age": 25}

d["name"]           # O(1) average
d["city"] = "NYC"   # O(1) average
d.get("x", None)    # O(1), safe access
del d["age"]        # O(1) average
"name" in d         # O(1) — checks keys
d.keys()            # O(1) — view object
d.values()          # O(1) — view object
d.items()           # O(1) — view object

# Iteration is O(n)
for k, v in d.items():
    print(k, v)
```

**Python 3.7+:** Dicts maintain insertion order.

---

## 3. Strings

```python
s = "hello world"

# Strings are IMMUTABLE
s[0]              # O(1)
s[1:4]            # O(k) where k = slice length
len(s)            # O(1)
s + "!"          # O(n+m) — creates new string
s.split()         # O(n)
s.join(lst)       # O(n)
s.strip()         # O(n)
s.replace("h","H")# O(n)
s.find("world")   # O(n*m) worst case
s[::-1]           # O(n) — reverse
s.lower()         # O(n)
s.upper()         # O(n)
s.isalpha()       # O(n)
s.isdigit()       # O(n)

# String formatting
f"Name is {name}"            # f-string (preferred)
"Name is {}".format(name)    # .format()
```

**Interview Tip:** Never build strings with `+=` in a loop — use `"".join(list)` instead (O(n) vs O(n²)).

---

## 4. List & Dict Comprehensions

```python
# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Dict comprehension
sq_dict = {x: x**2 for x in range(5)}

# Set comprehension
unique = {x % 3 for x in range(10)}

# Generator expression (memory efficient — lazy evaluation)
gen = (x**2 for x in range(1000000))  # doesn't store all in memory
```

---

## 5. Functions, *args, **kwargs, Scope

```python
# *args — variable positional arguments (tuple)
def add(*args):
    return sum(args)

add(1, 2, 3)  # 6

# **kwargs — variable keyword arguments (dict)
def info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

info(name="Alice", age=25)

# Combined
def func(a, b, *args, **kwargs):
    pass
```

### LEGB Scope Rule
```
L - Local (inside current function)
E - Enclosing (outer function, for nested functions)
G - Global (module level)
B - Built-in (Python built-ins)
```

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)  # "local"
    inner()

# Use `global` keyword to modify global var
# Use `nonlocal` keyword to modify enclosing var
```

---

## 6. Big-O Time Complexity Summary

| Complexity | Name | Example |
|-----------|------|---------|
| O(1) | Constant | Dict lookup, array index |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Loop through array |
| O(n log n) | Linearithmic | Merge sort, Timsort |
| O(n²) | Quadratic | Nested loops, bubble sort |
| O(2ⁿ) | Exponential | Recursive subsets |
| O(n!) | Factorial | Permutations |

---

## 7. Stacks & Queues

### Stack (LIFO) — Use list or collections.deque
```python
stack = []
stack.append(1)   # push — O(1)
stack.append(2)
stack.pop()       # pop — O(1), returns 2
stack[-1]         # peek — O(1)
```

### Queue (FIFO) — Use collections.deque
```python
from collections import deque
q = deque()
q.append(1)       # enqueue — O(1)
q.append(2)
q.popleft()       # dequeue — O(1), returns 1
```

**Never use `list.pop(0)` for queue — it's O(n). Use `deque`.**

---

## 8. Linked Lists

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Traversal: O(n)
# Insert at head: O(1)
# Insert at tail (no ref): O(n)
# Search: O(n)
# Delete (given node): O(1) if prev known, else O(n)
```

---

## 9. Hash Map Internals (dict)

- Uses hash table with open addressing
- `hash(key)` → index in internal array
- Collisions resolved by probing
- Load factor triggers resize (amortized O(1))
- Keys must be **hashable** (immutable types)

```python
# Custom hashable object
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __hash__(self):
        return hash((self.x, self.y))
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

---

## 10. Trees & Graphs

### Binary Tree
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Traversals — all O(n)
def inorder(root):    # Left → Root → Right (BST: sorted)
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):   # Root → Left → Right
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):  # Left → Right → Root
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
```

### BST Operations
| Operation | Average | Worst (unbalanced) |
|-----------|---------|---------------------|
| Search | O(log n) | O(n) |
| Insert | O(log n) | O(n) |
| Delete | O(log n) | O(n) |

### Graph Representation
```python
# Adjacency List (most common)
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

# BFS — O(V + E)
from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# DFS — O(V + E)
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

---

## 11. Popular DSA Patterns for Interviews

### Two Pointers
```python
# Find pair with target sum in sorted array
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
```

### Sliding Window
```python
# Max sum subarray of size k
def max_sum_k(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

### Binary Search
```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
# Time: O(log n)
```

### Recursion & Backtracking
```python
# Generate all subsets
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()  # backtrack
    backtrack(0, [])
    return result
```

---

## 12. Sorting Algorithms — Quick Reference

| Algorithm | Best | Average | Worst | Space | Stable? |
|-----------|------|---------|-------|-------|---------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Tim Sort (Python) | O(n) | O(n log n) | O(n log n) | O(n) | Yes |

---

## 13. Important Python Interview Snippets

### Lambda, Map, Filter, Reduce
```python
# Lambda
square = lambda x: x ** 2

# Map — apply function to all items
list(map(lambda x: x*2, [1,2,3]))  # [2, 4, 6]

# Filter — keep items where condition is True
list(filter(lambda x: x > 2, [1,2,3,4]))  # [3, 4]

# Reduce — accumulate
from functools import reduce
reduce(lambda a, b: a + b, [1,2,3,4])  # 10
```

### Collections Module
```python
from collections import Counter, defaultdict, OrderedDict, deque

# Counter
Counter("aabbbcc")  # Counter({'b':3, 'a':2, 'c':2})

# defaultdict
dd = defaultdict(list)
dd["key"].append(1)  # no KeyError

# deque — double-ended queue
d = deque([1,2,3])
d.appendleft(0)     # O(1)
d.pop()             # O(1)
d.popleft()         # O(1)
```

### Heap (Priority Queue)
```python
import heapq
h = []
heapq.heappush(h, 3)   # O(log n)
heapq.heappush(h, 1)
heapq.heappop(h)        # O(log n), returns 1 (min)
# Python only has min-heap. For max-heap, negate values.
heapq.nlargest(2, h)    # O(n log k)
```

---

## 14. OOP Basics for Interviews

```python
class Animal:
    def __init__(self, name):
        self.name = name        # instance variable

    def speak(self):
        raise NotImplementedError

class Dog(Animal):              # Inheritance
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Polymorphism
for animal in [Dog("Rex"), Cat("Whiskers")]:
    print(animal.speak())
```

### Dunder/Magic Methods
```python
__init__    # constructor
__str__     # print(obj)
__repr__    # repr(obj), debugging
__len__     # len(obj)
__eq__      # obj1 == obj2
__lt__      # obj1 < obj2 (for sorting)
__hash__    # hash(obj)
__iter__    # makes object iterable
__next__    # next value in iteration
```

---

## 15. Useful Built-in Functions

```python
enumerate(lst)         # (index, value) pairs
zip(lst1, lst2)        # pair elements
sorted(lst, key=...)   # returns new sorted list
reversed(lst)          # iterator in reverse
any([False, True])     # True — at least one True
all([True, True])      # True — all True
isinstance(x, int)     # type check
id(x)                  # memory address
type(x)                # type of object
dir(x)                 # list attributes/methods
```

---

