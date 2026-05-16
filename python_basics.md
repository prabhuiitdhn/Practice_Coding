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

### Why Are Strings Immutable in Python?

Strings in Python are immutable, meaning their value cannot be changed after they are created. This design choice is intentional and offers several advantages:

---

### **1. Memory Efficiency**
- **String Interning**: Python uses a technique called *string interning*, where identical string literals are stored only once in memory. This reduces memory usage and improves performance.
  - Example:
    ```python
    a = "hello"
    b = "hello"
    print(id(a) == id(b))  # True, both point to the same memory location
    ```
- If strings were mutable, modifying one would inadvertently affect all references to the same string, breaking this optimization.

---

### **2. Hashability**
- Immutable objects, like strings, are hashable. This means they can be used as keys in dictionaries or elements in sets.
  - Example:
    ```python
    my_dict = {"name": "Alice"}
    print(my_dict["name"])  # Works because strings are immutable and hashable
    ```
- If strings were mutable, their hash value could change, making them unreliable as dictionary keys or set elements.

---

### **3. Thread Safety**
- Immutability ensures that strings are thread-safe. Multiple threads can access the same string without worrying about one thread modifying it and causing inconsistencies for others.

---

### **4. Security**
- Strings are often used to store sensitive data, such as passwords or URLs. Immutability ensures that the original string cannot be accidentally or maliciously modified.

---

### **5. Predictable Behavior**
- Immutability makes strings easier to reason about. When you pass a string to a function, you can be confident that the function won't modify the original string.

---

### **6. Performance Optimization**
- Since strings are immutable, Python can optimize their usage in various ways:
  - **Caching**: Frequently used strings (like `"hello"`, `"world"`) are cached for reuse.
  - **Copy-on-Write**: Instead of copying strings, Python can safely share references to the same string.

---

### **How to Modify Strings in Python**
Although strings are immutable, you can create new strings based on existing ones:
1. **Concatenation**:
   ```python
   s = "hello"
   s = s + " world"  # Creates a new string
   print(s)  # "hello world"
   ```

2. **String Methods**:
   ```python
   s = "hello"
   s = s.upper()  # Creates a new string
   print(s)  # "HELLO"
   ```

3. **Using `join` for Efficiency**:
   - Avoid using `+=` in loops, as it creates a new string each time (O(n²) complexity). Use `"".join()` instead (O(n) complexity).
   ```python
   words = ["hello", "world"]
   result = " ".join(words)
   print(result)  # "hello world"
   ```

---

### **Key Takeaway**
The immutability of strings in Python is a deliberate design choice that enhances memory efficiency, performance, security, and reliability. While it may seem restrictive at first, Python provides efficient ways to create new strings when modifications are needed.

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

### Q&A: Mutable vs Immutable Data Types

**Q: What is the difference between mutable and immutable data types in Python?**

**A:**
1. **Definition**:
   - **Mutable**: Objects whose state (or data) can be changed after creation.
   - **Immutable**: Objects whose state cannot be changed once created.

2. **Examples**:
   - **Mutable**: `list`, `dict`, `set`, `bytearray`
   - **Immutable**: `int`, `float`, `str`, `tuple`, `frozenset`, `bool`, `bytes`

3. **Memory Behavior**:
   - **Mutable**: Changes are made in-place, and the object retains the same memory address.
   - **Immutable**: Any modification creates a new object with a different memory address.

   Example:
   ```python
   # Immutable
   x = 10
   print(id(x))  # Memory address of x
   x += 1
   print(id(x))  # New memory address

   # Mutable
   lst = [1, 2, 3]
   print(id(lst))  # Memory address of lst
   lst.append(4)
   print(id(lst))  # Same memory address
   ```

4. **Hashability**:
   - **Immutable**: Hashable (can be used as dictionary keys or set elements) because their value cannot change.
   - **Mutable**: Not hashable (cannot be used as dictionary keys) because their value can change, which would break the hash.

   Example:
   ```python
   # Immutable as dictionary keys
   my_dict = {(1, 2): "tuple_key"}  # Works because tuple is immutable

   # Mutable as dictionary keys
   my_dict = {[1, 2]: "list_key"}  # Raises TypeError because list is mutable
   ```

5. **Thread Safety**:
   - **Immutable**: Safer in multi-threaded environments because their state cannot be modified by other threads.
   - **Mutable**: Require synchronization mechanisms to avoid race conditions.

6. **Performance**:
   - **Immutable**: Faster to access because their state is fixed.
   - **Mutable**: Slower due to the overhead of managing changes.

---

### Implications for Machine Learning

1. **Data Integrity**:
   - Immutable types like `tuple` or `frozenset` are useful for ensuring that critical data (e.g., hyperparameters, configurations) remains unchanged throughout the pipeline.

2. **Hashability in Sets and Dictionaries**:
   - Immutable types are essential when using sets or dictionaries for tasks like caching results, memoization, or creating lookup tables.

   Example:
   ```python
   # Caching results
   cache = {}
   def expensive_computation(params):
       if params in cache:
           return cache[params]
       result = sum(params)  # Simulate computation
       cache[params] = result
       return result

   print(expensive_computation((1, 2, 3)))  # Works because tuple is immutable
   ```

3. **Avoiding Bugs in Data Pipelines**:
   - Mutable objects can lead to unintended side effects when passed between functions or threads. For example, modifying a list in one part of the pipeline might affect other parts.

   Example:
   ```python
   def preprocess(data):
       data.append(0)  # Modifies the original list
       return data

   original_data = [1, 2, 3]
   processed_data = preprocess(original_data)
   print(original_data)  # [1, 2, 3, 0] — original data is modified!
   ```

   To avoid this, use immutable types or explicitly copy mutable objects:
   ```python
   def preprocess(data):
       data = data.copy()  # Create a copy to avoid modifying the original
       data.append(0)
       return data
   ```

4. **Performance Optimization**:
   - Immutable types like `bytes` are often used for large datasets or binary data because they are memory-efficient and faster to process.

5. **Concurrency**:
   - Immutable objects are preferred in distributed systems or parallel processing (e.g., using `multiprocessing` or `Ray`) to avoid synchronization issues.

---

**Key Takeaways for ML Engineers**:
- Use **immutable types** for:
  - Hyperparameters, configurations, and keys in dictionaries.
  - Ensuring data integrity in pipelines.
  - Thread-safe operations in multi-threaded or distributed environments.
- Use **mutable types** for:
  - Data structures that require frequent updates (e.g., training batches, intermediate results).
  - Caching or memoization where immutability is not required.

---

### Q&A: String Interning in Python

**Q: What is string interning, and how does it work in Python?**

**A:**
String interning is an optimization technique used by Python to save memory and improve performance. It ensures that identical string literals are stored only once in memory, rather than creating multiple copies of the same string. This is particularly useful for immutable objects like strings, as they cannot be modified after creation.

---

### **How String Interning Works**
1. **String Pool**:
   - Python maintains a pool of "interned" strings. These are strings that are stored in memory and reused whenever the same string literal is encountered.
   - For example:
     ```python
     a = "hello"
     b = "hello"
     print(id(a) == id(b))  # True, both point to the same memory location
     ```

2. **Automatic Interning**:
   - Python automatically interns certain strings, such as:
     - Strings that look like identifiers (e.g., `"hello"`, `"world"`, `"abc123"`).
     - Strings that are short and consist of alphanumeric characters.
   - Example:
     ```python
     x = "data"
     y = "data"
     print(x is y)  # True, both refer to the same interned string
     ```

3. **Explicit Interning**:
   - You can explicitly intern strings using the `sys.intern()` function. This is useful for strings that are not automatically interned.
   - Example:
     ```python
     import sys
     a = sys.intern("machine learning")
     b = sys.intern("machine learning")
     print(a is b)  # True
     ```

---

### **Why String Interning Matters for ML Engineers**

1. **Memory Optimization**:
   - In machine learning, large datasets often involve repetitive string values (e.g., feature names, labels, or categorical data). String interning reduces memory usage by ensuring that identical strings are stored only once.
   - Example:
     ```python
     labels = ["cat", "dog", "cat", "dog", "cat"]
     # Without interning, each "cat" and "dog" would occupy separate memory.
     ```

2. **Performance Improvement**:
   - String comparisons are faster when strings are interned because Python can compare their memory addresses (`is`) instead of their content (`==`).
   - Example:
     ```python
     a = "feature1"
     b = "feature1"
     print(a is b)  # True, faster comparison
     ```

3. **Efficient Categorical Encoding**:
   - When working with categorical data, interning can be used to optimize memory and speed up operations like one-hot encoding or label encoding.

---

### **When to Use String Interning**
1. **Repetitive Strings**:
   - If your application involves repetitive string values (e.g., column names, labels, or keys in dictionaries), interning can save memory.

2. **Large-Scale Data Processing**:
   - In ML pipelines, where strings are used extensively for metadata or feature names, interning can improve performance.

3. **Custom String Handling**:
   - Use `sys.intern()` for strings that are dynamically generated but frequently reused.

---

### **Example: String Interning in Practice**
```python
import sys

# Without interning
a = "machine learning"
b = "machine learning"
print(a is b)  # False, different memory locations

# With interning
a = sys.intern("machine learning")
b = sys.intern("machine learning")
print(a is b)  # True, same memory location
```

---

### **Key Takeaways**
- String interning is a memory and performance optimization technique.
- It is particularly useful in scenarios involving repetitive strings, such as ML pipelines with categorical data or feature names.
- Use `sys.intern()` explicitly for dynamically generated strings to ensure they are interned.

---

### Q&A: Memory Handling for Mutable and Immutable Objects

**Q: How does Python handle memory for mutable and immutable objects?**

**A:**
Python handles memory for mutable and immutable objects differently due to their distinct characteristics. Here's a detailed explanation:

---

### **1. Immutable Objects**
Immutable objects are those whose state cannot be changed after they are created. Examples include `int`, `float`, `str`, `tuple`, and `frozenset`.

#### **Memory Handling for Immutable Objects**
- **Single Memory Allocation**:
  - When you create an immutable object, Python allocates memory for it and stores its value.
  - If another variable is assigned the same value, Python reuses the existing memory instead of creating a new object. This is known as **object interning** (applies to small integers, strings, etc.).
  - Example:
    ```python
    a = 10
    b = 10
    print(id(a) == id(b))  # True, both point to the same memory location
    ```

- **Copy-on-Write**:
  - Since immutable objects cannot be modified, any operation that appears to change their value actually creates a new object in memory.
  - Example:
    ```python
    x = "hello"
    y = x + " world"  # Creates a new string object
    print(id(x) == id(y))  # False, different memory locations
    ```

- **Garbage Collection**:
  - When an immutable object is no longer referenced, Python's garbage collector deallocates its memory.

---

### **2. Mutable Objects**
Mutable objects are those whose state can be changed after they are created. Examples include `list`, `dict`, `set`, and `bytearray`.

#### **Memory Handling for Mutable Objects**
- **Single Memory Allocation**:
  - When you create a mutable object, Python allocates memory for it and allows modifications in-place.
  - Example:
    ```python
    lst = [1, 2, 3]
    lst.append(4)  # Modifies the same object in memory
    ```

- **Shared References**:
  - If multiple variables reference the same mutable object, changes made through one variable affect all others.
  - Example:
    ```python
    a = [1, 2, 3]
    b = a
    b.append(4)
    print(a)  # [1, 2, 3, 4] — both `a` and `b` point to the same object
    ```

- **Garbage Collection**:
  - Similar to immutable objects, when a mutable object is no longer referenced, Python's garbage collector deallocates its memory.

---

### **Key Differences in Memory Handling**

| Aspect                  | Immutable Objects                  | Mutable Objects                  |
|-------------------------|-------------------------------------|-----------------------------------|
| **Modification**        | Creates a new object               | Modifies the same object         |
| **Memory Reuse**        | Reuses memory for identical values | No memory reuse                  |
| **Thread Safety**       | Thread-safe                        | Not thread-safe                  |
| **Hashability**         | Hashable (can be dict keys)        | Not hashable                     |

---

### **Why This Matters**
1. **Performance**:
   - Immutable objects are faster to access because their state is fixed.
   - Mutable objects have overhead due to their modifiable nature.

2. **Safety**:
   - Immutable objects are safer to use in multi-threaded environments because their state cannot change unexpectedly.

3. **Design**:
   - Use immutable objects for data that should not change (e.g., keys in dictionaries).
   - Use mutable objects for data that requires frequent updates (e.g., lists of results).

---

### Q&A: Modifying Immutable Objects

**Q: What happens when you modify an immutable object like an integer or string?**

**A:**
Immutable objects in Python, such as integers and strings, cannot be modified after they are created. However, when you perform an operation that appears to "modify" an immutable object, Python creates a **new object** in memory instead of altering the original object. Here's a detailed explanation:

---

### **1. Immutable Objects Cannot Be Changed**
- Immutable objects, like integers and strings, have a fixed memory allocation once they are created.
- Any operation that seems to modify their value actually results in the creation of a **new object**.

---

### **2. Example: Modifying an Integer**
```python
x = 10
print(id(x))  # Memory address of x

x = x + 1  # Creates a new integer object
print(id(x))  # New memory address
```
- In this example:
  - Initially, `x` points to the memory location of the integer `10`.
  - When `x + 1` is executed, Python creates a new integer object with the value `11` and assigns it to `x`.
  - The original object (`10`) remains unchanged, and `x` now points to the new object.

---

### **3. Example: Modifying a String**
```python
s = "hello"
print(id(s))  # Memory address of s

s = s + " world"  # Creates a new string object
print(id(s))  # New memory address
```
- In this example:
  - Initially, `s` points to the memory location of the string `"hello"`.
  - When `s + " world"` is executed, Python creates a new string object with the value `"hello world"` and assigns it to `s`.
  - The original string (`"hello"`) remains unchanged, and `s` now points to the new object.

---

### **4. Why Does Python Create a New Object?**
- **Memory Efficiency**:
  - Immutable objects are often reused in memory to save space. For example, small integers and strings are interned (stored in a shared pool).
  - Modifying an immutable object would break this optimization, so Python creates a new object instead.

- **Hashability**:
  - Immutable objects are hashable, meaning their value can be used as a key in dictionaries or as elements in sets.
  - If their value could change, their hash would also change, making them unreliable as dictionary keys.

- **Thread Safety**:
  - Immutability ensures that objects cannot be modified by multiple threads, making them safer in concurrent programming.

---

### **5. Key Takeaways**
- Modifying an immutable object creates a **new object** in memory.
- The original object remains unchanged.
- This behavior ensures memory efficiency, hashability, and thread safety.

---

### Q&A: Mutable vs Immutable Data Types

**Q: Which built-in data types in Python are mutable and which are immutable?**

**A:**
In Python, data types are categorized as **mutable** or **immutable** based on whether their value can be changed after creation. Here's a detailed explanation:

---

### **1. Mutable Data Types**
Mutable data types are those whose values can be changed in place after they are created. This means you can modify their content without creating a new object.

#### **Examples of Mutable Data Types**:
1. **List**:
   - Example:
     ```python
     lst = [1, 2, 3]
     lst.append(4)  # Modifies the same object
     print(lst)  # [1, 2, 3, 4]
     ```

2. **Dictionary**:
   - Example:
     ```python
     d = {"name": "Alice", "age": 25}
     d["age"] = 26  # Modifies the same object
     print(d)  # {'name': 'Alice', 'age': 26}
     ```

3. **Set**:
   - Example:
     ```python
     s = {1, 2, 3}
     s.add(4)  # Modifies the same object
     print(s)  # {1, 2, 3, 4}
     ```

4. **Bytearray**:
   - Example:
     ```python
     b = bytearray(b"hello")
     b[0] = 72  # Modifies the same object
     print(b)  # bytearray(b'Hello')
     ```

---

### **2. Immutable Data Types**
Immutable data types are those whose values cannot be changed after they are created. Any operation that appears to modify their value actually creates a new object.

#### **Examples of Immutable Data Types**:
1. **Integer (`int`)**:
   - Example:
     ```python
     x = 10
     x = x + 1  # Creates a new object
     print(x)  # 11
     ```

2. **Float (`float`)**:
   - Example:
     ```python
     f = 3.14
     f = f + 1.0  # Creates a new object
     print(f)  # 4.14
     ```

3. **String (`str`)**:
   - Example:
     ```python
     s = "hello"
     s = s + " world"  # Creates a new object
     print(s)  # "hello world"
     ```

4. **Tuple (`tuple`)**:
   - Example:
     ```python
     t = (1, 2, 3)
     # t[0] = 0  # Raises TypeError: 'tuple' object does not support item assignment
     ```

5. **Frozenset (`frozenset`)**:
   - Example:
     ```python
     fs = frozenset([1, 2, 3])
     # fs.add(4)  # Raises AttributeError: 'frozenset' object has no attribute 'add'
     ```

6. **Boolean (`bool`)**:
   - Example:
     ```python
     b = True
     b = not b  # Creates a new object
     print(b)  # False
     ```

7. **Bytes (`bytes`)**:
   - Example:
     ```python
     b = b"hello"
     # b[0] = 72  # Raises TypeError: 'bytes' object does not support item assignment
     ```

---

### **Key Differences Between Mutable and Immutable Data Types**

| Aspect                  | Mutable Data Types                   | Immutable Data Types                              |
|-------------------------|---------------------------------------|---------------------------------------------------|
| **Modification**        | Can be modified in place             | Cannot be modified in place                       |
| **Memory Behavior**     | Same object is updated               | New object is created                             |
| **Hashability**         | Not hashable                         | Hashable (can be dict keys)                       |
| **Examples**            | `list`, `dict`, `set`, `bytearray`   | `int`, `float`, `str`, `tuple`, `frozenset`, `bool`, `bytes` |

---

### **Why This Matters**
1. **Performance**:
   - Immutable objects are faster to access because their state is fixed.
   - Mutable objects have overhead due to their modifiable nature.

2. **Thread Safety**:
   - Immutable objects are safer in multi-threaded environments because their state cannot change unexpectedly.

3. **Design**:
   - Use mutable objects for data that requires frequent updates.
   - Use immutable objects for data that should remain constant (e.g., dictionary keys).

