"""
https://www.geeksforgeeks.org/introduction-to-greedy-algorithm-data-structures-and-algorithm-tutorials/

The greedy algorithm method is used for optimisation. where goal is to make the locally optimal choices at each stage
with the hope of finding a global optimum.

It is called “greedy” because it tries to find the best solution by making
the best choice at each step, without considering future steps or the consequences of the current decision. common
use cases:

1. Scheduling and Resource Allocation:The greedy algorithm can be used to schedule jobs or allocate resources in an efficient manner.
2. minimum spanning trees
3. coin change problem
4. Huffman coding

It’s important to note that not all optimization problems can be solved by a greedy algorithm, and there are cases
where the greedy approach can lead to suboptimal solutions. However, in many cases, the greedy algorithm provides a
good approximation to the optimal solution and is a useful tool for solving optimization problems quickly and
efficiently.

All greedy algorithms follow a basic structure:
1. Declare an empty result = 0.
2. We make a greedy choice to select, If the choice is feasible add it to the final result.
3. return the result.

Greedy algorithm and Dynamic programming are two of the most widely used algorithm paradigms for solving complex
programming problems, While Greedy approach works for problems where local optimal choice leads to global optimal
solution Dynamic Programming works for problems having overlapping sub problems structure where answer to a sub problem
is needed for solving several other sub problems. Detailed differences are given in the table below: feature:


1. in greedy algorithm, we make whatever choice are better at the moment without thinking about the global optimal
solution

2. in greedy, sometimes there is no such guarantee of getting Optimal Solution.
3. A greedy method follows the problem solving heuristic of making the locally optimal choice at each stage.
4. It is more efficient in terms of memory as it never look back or revise previous choices
5. Greedy methods are generally faster. For example, Dijkstra’s shortest path algorithm takes O(ELogV + VLogV) time.
6. The greedy method computes its solution by making its choices in a serial forward fashion, never looking back or
revising previous choices."""