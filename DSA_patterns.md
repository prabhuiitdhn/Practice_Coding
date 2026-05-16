### Key DSA (Data Structures and Algorithms) Patterns for Interviews

When preparing for coding interviews, it is essential to recognize common problem-solving patterns. These patterns help you identify the right approach to solve a problem efficiently. Below are some of the most important DSA patterns used in interviews:

---

#### 1. **Sliding Window**:
   - **Description**: This pattern is used to solve problems involving a contiguous subarray or substring. It involves maintaining a window (range of elements) and sliding it across the data structure to find the optimal solution.
   - **Common Problems**:
     - Maximum sum of a subarray of size `k`.
     - Longest substring without repeating characters.
     - Minimum window substring.
   - **Example**:
     ```python
     def max_sum_subarray(arr, k):
         max_sum, window_sum = 0, 0
         for i in range(len(arr)):
             window_sum += arr[i]
             if i >= k - 1:
                 max_sum = max(max_sum, window_sum)
                 window_sum -= arr[i - (k - 1)]
         return max_sum
     ```

---

#### 2. **Two Pointers**:
   - **Description**: This pattern uses two pointers to solve problems involving sorted arrays, linked lists, or strings. The pointers move toward each other or in the same direction to find a solution.
   - **Common Problems**:
     - Pair with a given sum in a sorted array.
     - Remove duplicates from a sorted array.
     - Container with most water.
   - **Example**:
     ```python
     def two_sum_sorted(arr, target):
         left, right = 0, len(arr) - 1
         while left < right:
             current_sum = arr[left] + arr[right]
             if current_sum == target:
                 return [left, right]
             elif current_sum < target:
                 left += 1
             else:
                 right -= 1
         return []
     ```

---

#### 3. **Fast and Slow Pointers**:
   - **Description**: This pattern is used to detect cycles in linked lists or arrays. It involves two pointers moving at different speeds.
   - **Common Problems**:
     - Detect a cycle in a linked list.
     - Find the middle of a linked list.
     - Find the starting point of a cycle.
   - **Example**:
     ```python
     def has_cycle(head):
         slow, fast = head, head
         while fast and fast.next:
             slow = slow.next
             fast = fast.next.next
             if slow == fast:
                 return True
         return False
     ```

---

#### 4. **Merge Intervals**:
   - **Description**: This pattern is used to solve problems involving overlapping intervals. It involves sorting the intervals and merging them based on their start and end times.
   - **Common Problems**:
     - Merge overlapping intervals.
     - Insert an interval.
     - Employee free time.
   - **Example**:
     ```python
     def merge_intervals(intervals):
         intervals.sort(key=lambda x: x[0])
         merged = [intervals[0]]
         for start, end in intervals[1:]:
             if start <= merged[-1][1]:
                 merged[-1][1] = max(merged[-1][1], end)
             else:
                 merged.append([start, end])
         return merged
     ```

---

#### 5. **Cyclic Sort**:
   - **Description**: This pattern is used to solve problems involving numbers in a given range (e.g., 1 to `n`). It involves placing numbers at their correct indices.
   - **Common Problems**:
     - Find the missing number.
     - Find all duplicate numbers.
     - Find the smallest missing positive number.
   - **Example**:
     ```python
     def cyclic_sort(nums):
         i = 0
         while i < len(nums):
             correct = nums[i] - 1
             if nums[i] != nums[correct]:
                 nums[i], nums[correct] = nums[correct], nums[i]
             else:
                 i += 1
         return nums
     ```

---

#### 6. **Top-K Elements**:
   - **Description**: This pattern is used to solve problems involving finding the top `k` largest or smallest elements. It often uses heaps or sorting.
   - **Common Problems**:
     - Kth largest element in an array.
     - Top K frequent elements.
     - K closest points to the origin.
   - **Example**:
     ```python
     import heapq
     def find_k_largest(nums, k):
         return heapq.nlargest(k, nums)
     ```

---

#### 7. **Binary Search**:
   - **Description**: This pattern is used to solve problems involving sorted arrays or search spaces. It involves dividing the search space in half at each step.
   - **Common Problems**:
     - Search in a rotated sorted array.
     - Find the peak element.
     - Find the square root of a number.
   - **Example**:
     ```python
     def binary_search(arr, target):
         left, right = 0, len(arr) - 1
         while left <= right:
             mid = (left + right) // 2
             if arr[mid] == target:
                 return mid
             elif arr[mid] < target:
                 left = mid + 1
             else:
                 right = mid - 1
         return -1
     ```

---

#### 8. **Dynamic Programming**:
   - **Description**: This pattern is used to solve problems by breaking them into overlapping subproblems and storing the results of subproblems to avoid redundant computations.
   - **Common Problems**:
     - Longest common subsequence.
     - Knapsack problem.
     - Fibonacci numbers.
   - **Example**:
     ```python
     def fibonacci(n):
         dp = [0, 1]
         for i in range(2, n + 1):
             dp.append(dp[i - 1] + dp[i - 2])
         return dp[n]
     ```

---

#### 9. **Backtracking**:
   - **Description**: This pattern is used to solve problems involving all possible combinations or permutations. It involves exploring all options and backtracking when a solution is invalid.
   - **Common Problems**:
     - N-Queens problem.
     - Subset sum problem.
     - Generate all permutations.
   - **Example**:
     ```python
     def generate_permutations(nums):
         result = []
         def backtrack(path, remaining):
             if not remaining:
                 result.append(path)
                 return
             for i in range(len(remaining)):
                 backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
         backtrack([], nums)
         return result
     ```

---

#### 10. **Graph Traversal**:
   - **Description**: This pattern is used to solve problems involving graphs. It involves traversing the graph using DFS or BFS.
   - **Common Problems**:
     - Find all paths in a graph.
     - Detect cycles in a graph.
     - Shortest path in an unweighted graph.
   - **Example**:
     ```python
     from collections import deque
     def bfs(graph, start):
         visited = set()
         queue = deque([start])
         while queue:
             node = queue.popleft()
             if node not in visited:
                 visited.add(node)
                 queue.extend(graph[node])
         return visited
     ```

---

These patterns are essential for solving a wide range of problems in coding interviews.

#### Question: What is the Merge Intervals Pattern?

**Answer**:

The **Merge Intervals** pattern is a common approach used to solve problems involving overlapping intervals. The idea is to sort the intervals based on their start times and then merge overlapping intervals by comparing their start and end times.

---

#### **Description**:
- This pattern is used when you need to process or merge overlapping intervals.
- The intervals are first sorted by their start times.
- As you iterate through the intervals, you compare the current interval with the previous one to check for overlaps.
- If the intervals overlap, they are merged into one interval.
- If they do not overlap, the current interval is added to the result as a separate interval.

---

#### **Steps to Solve**:
1. **Sort the Intervals**:
   - Sort the intervals based on their start times.
2. **Iterate Through the Intervals**:
   - Compare the current interval with the last merged interval.
   - If they overlap, merge them by updating the end time of the last merged interval.
   - If they do not overlap, add the current interval to the result.
3. **Return the Result**:
   - The result will contain all the merged intervals.

---

#### **Common Problems**:
1. **Merge Overlapping Intervals**:
   - Combine all overlapping intervals into one.
2. **Insert an Interval**:
   - Insert a new interval into a list of sorted intervals and merge if necessary.
3. **Employee Free Time**:
   - Find the free time intervals when no employee is working.

---

#### **Example: Merge Overlapping Intervals**:
```python
def merge_intervals(intervals):
    # Step 1: Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    # Step 2: Initialize the result with the first interval
    merged = [intervals[0]]
    
    # Step 3: Iterate through the intervals
    for start, end in intervals[1:]:
        # Compare with the last interval in the result
        if start <= merged[-1][1]:  # Overlapping intervals
            merged[-1][1] = max(merged[-1][1], end)  # Merge intervals
        else:
            merged.append([start, end])  # Add non-overlapping interval
    
    return merged

# Example Usage
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))
# Output: [[1, 6], [8, 10], [15, 18]]
```

---

#### **Example: Insert an Interval**:
```python
def insert_interval(intervals, new_interval):
    result = []
    for i, (start, end) in enumerate(intervals):
        if new_interval[1] < start:  # New interval comes before the current interval
            result.append(new_interval)
            return result + intervals[i:]
        elif new_interval[0] > end:  # New interval comes after the current interval
            result.append([start, end])
        else:  # Overlapping intervals
            new_interval = [min(new_interval[0], start), max(new_interval[1], end)]
    result.append(new_interval)
    return result

# Example Usage
intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
print(insert_interval(intervals, new_interval))
# Output: [[1, 5], [6, 9]]
```

---

#### **Example: Employee Free Time**:
```python
def employee_free_time(schedule):
    # Flatten the schedule and sort intervals
    intervals = sorted([interval for employee in schedule for interval in employee], key=lambda x: x[0])
    
    # Merge intervals
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    
    # Find gaps between merged intervals
    free_time = []
    for i in range(1, len(merged)):
        free_time.append([merged[i-1][1], merged[i][0]])
    
    return free_time

# Example Usage
schedule = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]
print(employee_free_time(schedule))
# Output: [[5, 6], [7, 9]]
```

---

#### **Key Points**:
1. **Sorting**:
   - Sorting the intervals by their start times is the first step in most problems involving intervals.
2. **Merging Logic**:
   - Overlapping intervals are merged by taking the maximum of their end times.
3. **Edge Cases**:
   - Empty intervals list.
   - Intervals that do not overlap at all.