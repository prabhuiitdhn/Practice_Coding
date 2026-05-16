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

---

### Q&A: Python Memory Optimization for Immutable Objects

**Q: How does Python optimize memory usage for immutable objects like integers and strings?**

**A:**
Python employs several optimization techniques to manage memory efficiently for immutable objects such as integers and strings. These techniques ensure that memory usage is minimized and performance is improved.

---

### **1. Object Interning**
Object interning is a mechanism where Python reuses memory for certain immutable objects instead of creating new ones. This is particularly useful for frequently used values.

#### **Examples of Interning**:
1. **Small Integers**:
   - Python preallocates and reuses integer objects in the range `-5` to `256`.
   - Example:
     ```python
     a = 100
     b = 100
     print(a is b)  # True, both refer to the same object
     ```

2. **Strings**:
   - Strings that are short and consist of alphanumeric characters are automatically interned.
   - Example:
     ```python
     x = "hello"
     y = "hello"
     print(x is y)  # True, both refer to the same object
     ```

3. **Explicit String Interning**:
   - For strings that are not automatically interned, you can use the `sys.intern()` function to intern them manually.
   - Example:
     ```python
     import sys
     s1 = sys.intern("long string example")
     s2 = sys.intern("long string example")
     print(s1 is s2)  # True
     ```

---

### **2. Shared References**
- Immutable objects are safe to share between variables because their value cannot change.
- When you assign an immutable object to multiple variables, Python reuses the same memory reference.
- Example:
  ```python
  a = "immutable"
  b = "immutable"
  print(id(a) == id(b))  # True, both share the same memory
  ```

---

### **3. Copy-on-Write**
- When you perform an operation on an immutable object, Python creates a new object only if the value changes.
- This avoids unnecessary memory allocation for operations that do not modify the object.
- Example:
  ```python
  s = "hello"
  t = s  # No new object is created
  s = s + " world"  # New object is created
  print(id(s) == id(t))  # False
  ```

---

### **4. Garbage Collection**
- Python uses a garbage collector to free memory occupied by objects that are no longer referenced.
- Immutable objects that are no longer needed are deallocated, ensuring efficient memory usage.

---

### **5. String Interning in Practice**
- Python optimizes memory usage for strings by maintaining a pool of interned strings.
- This is particularly useful for identifiers, keywords, and frequently used strings.
- Example:
  ```python
  keyword = "def"
  another_keyword = "def"
  print(keyword is another_keyword)  # True
  ```

---

### **6. Why These Optimizations Matter**
1. **Memory Efficiency**:
   - Reusing objects reduces memory consumption, especially for frequently used values like small integers and common strings.

2. **Performance**:
   - Comparing interned objects is faster because Python can compare their memory addresses (`is`) instead of their content (`==`).

3. **Thread Safety**:
   - Immutable objects are inherently thread-safe, making them ideal for shared data in multi-threaded applications.

---

### **Key Takeaways**
- Python optimizes memory usage for immutable objects through interning, shared references, and garbage collection.
- These optimizations improve performance and reduce memory overhead, especially for frequently used values like small integers and strings.

---

### Q&A: `is` vs `==` in Python

**Q: What is the difference between `is` and `==` in Python? How does it relate to mutability?**

**A:**

---

### **1. `is` Operator**
- The `is` operator checks **identity**, i.e., whether two variables refer to the **same object** in memory.
- It compares the memory addresses of the objects.

#### **Example**:
```python
a = [1, 2, 3]
b = a
print(a is b)  # True, both refer to the same object
```

#### **Key Points**:
- `is` returns `True` only if both variables point to the same memory location.
- It is often used to check for **singleton objects** like `None`.
  ```python
  x = None
  print(x is None)  # True
  ```

---

### **2. `==` Operator**
- The `==` operator checks **equality**, i.e., whether two objects have the **same value**.
- It compares the content of the objects, not their memory addresses.

#### **Example**:
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True, both have the same content
print(a is b)  # False, they are different objects in memory
```

#### **Key Points**:
- `==` returns `True` if the values of the objects are equal, even if they are stored in different memory locations.
- It is used for value comparison.

---

### **3. Relation to Mutability**
The behavior of `is` and `==` is closely related to whether an object is mutable or immutable:

#### **Immutable Objects**:
- For immutable objects like `int`, `float`, `str`, and `tuple`, Python often reuses memory for objects with the same value (object interning).
- This means `is` and `==` may both return `True` for small integers or short strings.
  ```python
  x = 100
  y = 100
  print(x is y)  # True, both refer to the same object
  print(x == y)  # True, values are equal
  ```

#### **Mutable Objects**:
- For mutable objects like `list`, `dict`, and `set`, Python creates a new object in memory even if the content is the same.
- This means `is` will return `False` for two objects with the same value, while `==` will return `True`.
  ```python
  a = [1, 2, 3]
  b = [1, 2, 3]
  print(a is b)  # False, different objects in memory
  print(a == b)  # True, values are equal
  ```

---

### **When to Use `is` vs `==`**
1. **Use `is`**:
   - When checking for **identity** (e.g., whether two variables point to the same object).
   - Commonly used for singletons like `None`:
     ```python
     if x is None:
         print("x is None")
     ```

2. **Use `==`**:
   - When checking for **equality** (e.g., whether two objects have the same value).
   - Commonly used for comparing strings, numbers, lists, etc.:
     ```python
     if a == b:
         print("a and b have the same value")
     ```

---

### **Key Takeaways**
- `is` checks **identity** (same memory location), while `==` checks **equality** (same value).
- For immutable objects, `is` may return `True` due to object interning.
- For mutable objects, `is` usually returns `False` unless explicitly assigned to the same object.

---

### Q&A: `hash()` Function and Mutability

**Q: What is the role of the `hash()` function in determining whether an object is mutable or immutable?**

**A:**

---

### **1. What is `hash()`?**
- The `hash()` function returns an integer that represents the hash value of an object.
- A hash value is a fixed-size integer that uniquely identifies an object based on its content.
- Hash values are used in data structures like **dictionaries** and **sets** to quickly locate keys.

#### **Example**:
```python
x = "hello"
print(hash(x))  # Outputs a hash value for the string "hello"
```

---

### **2. Hashability and Immutability**
- **Immutable objects** are hashable because their content cannot change after creation. This ensures that their hash value remains constant throughout their lifetime.
- **Mutable objects** are not hashable because their content can change, which would invalidate their hash value and break the integrity of hash-based data structures.

#### **Examples**:
1. **Immutable Objects (Hashable)**:
   - `int`, `float`, `str`, `tuple`, `frozenset` are hashable.
   - Example:
     ```python
     x = 42
     print(hash(x))  # Outputs a hash value
     y = "immutable"
     print(hash(y))  # Outputs a hash value
     ```

2. **Mutable Objects (Not Hashable)**:
   - `list`, `dict`, `set`, `bytearray` are not hashable.
   - Example:
     ```python
     lst = [1, 2, 3]
     print(hash(lst))  # Raises TypeError: unhashable type: 'list'
     ```

---

### **3. Why Are Mutable Objects Not Hashable?**
- **Consistency**:
  - Hash values must remain constant for the lifetime of an object. If a mutable object were hashable, modifying its content would change its hash value, leading to inconsistencies in hash-based data structures like dictionaries and sets.

- **Integrity**:
  - Hash-based data structures rely on the hash value to locate objects. If the hash value changes, the object would become "lost" in the data structure.

#### **Example**:
```python
# Immutable object as a dictionary key
my_dict = {(1, 2): "tuple_key"}  # Works because tuple is immutable

# Mutable object as a dictionary key
my_dict = {[1, 2]: "list_key"}  # Raises TypeError: unhashable type: 'list'
```

---

### **4. Relation to Mutability**
- **Immutable Objects**:
  - Their hash value is based on their content, which cannot change. This makes them reliable for use as dictionary keys or set elements.
  - Example:
    ```python
    t = (1, 2, 3)
    print(hash(t))  # Outputs a hash value
    ```

- **Mutable Objects**:
  - They are not hashable because their content can change, which would invalidate their hash value.
  - Example:
    ```python
    s = {1, 2, 3}
    print(hash(s))  # Raises TypeError: unhashable type: 'set'
    ```

---

### **5. Special Case: `tuple`**
- A `tuple` is immutable and hashable **only if all its elements are hashable**.
- Example:
  ```python
  t1 = (1, 2, 3)
  print(hash(t1))  # Outputs a hash value

  t2 = ([1, 2], 3)
  print(hash(t2))  # Raises TypeError: unhashable type: 'list'
  ```

---

### **6. Why This Matters**
1. **Performance**:
   - Hashable objects allow for fast lookups in dictionaries and sets.
   - Immutable objects are preferred for keys in hash-based data structures.

2. **Design**:
   - Use immutable objects when you need reliable hash values (e.g., keys in dictionaries).
   - Avoid using mutable objects in situations where hashability is required.

---

### **Key Takeaways**
- The `hash()` function determines whether an object is hashable.
- Immutable objects are hashable because their content cannot change, ensuring consistent hash values.
- Mutable objects are not hashable because their content can change, which would invalidate their hash value.

---

### Q&A: Mutability — Senior-Level Interview Questions

---

**Q1: When would you use a tuple instead of a list?**

Tuples are used instead of lists when the data is **fixed** and should not be modified. Since tuples are immutable, they are more memory-efficient and faster to access compared to lists. They are ideal for representing **heterogeneous data** (e.g., coordinates, database records) or when the data needs to be used as a **dictionary key** or stored in a **set**. For example, tuples are commonly used to represent rows in a database or as return values for functions that need to return multiple values.

---

**Q2: Why are dictionary keys required to be immutable?**

Dictionary keys must be immutable because their hash value is used to determine their location in the hash table. If a key were mutable, its hash value could change after insertion, making it impossible to locate the key in the dictionary. This would break the integrity of the dictionary. Immutable objects like strings, numbers, and tuples ensure that the hash value remains constant, allowing dictionaries to maintain their performance and reliability.

---

**Q3: How does immutability help in multi-threaded programming?**

Immutability ensures that objects cannot be modified after creation, making them inherently **thread-safe**. In multi-threaded environments, multiple threads can safely access immutable objects without the risk of one thread modifying the object and causing inconsistencies for others. This eliminates the need for synchronization mechanisms like locks, reducing complexity and improving performance. For example, using immutable data structures for shared configuration or constants ensures that all threads see a consistent view of the data.

---

**Q4: What are the implications of mutability when using default arguments in functions?**

Using mutable default arguments in functions can lead to **unexpected behavior** because the default value is shared across all calls to the function. If the mutable object is modified, the changes persist across subsequent calls. This can cause subtle bugs that are difficult to debug. For example:
```python
def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [1, 2] — unexpected behavior
```
To avoid this, use `None` as the default value and initialize the mutable object inside the function:
```python
def append_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst
```

---

**Q5: How can you ensure that a function does not modify a mutable argument passed to it?**

To prevent a function from modifying a mutable argument, you can create a **copy** of the object inside the function. This ensures that the original object remains unchanged. For example:
```python
def process_list(lst):
    lst_copy = lst.copy()  # Create a shallow copy
    lst_copy.append(100)   # Modify the copy
    return lst_copy

original = [1, 2, 3]
result = process_list(original)
print(original)  # [1, 2, 3] — original remains unchanged
```
For nested or deeply nested structures, use `copy.deepcopy()` to create a deep copy. Alternatively, you can use **immutable data structures** like tuples or frozensets to ensure that the data cannot be modified.

