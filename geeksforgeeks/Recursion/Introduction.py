"""
https://www.geeksforgeeks.org/introduction-to-recursion-data-structure-and-algorithm-tutorials/



1. recursion solves a particular problems by calling a copy of itself and solving smaller subproblems of the
original problems.

2. It should also provide a certain case in order to terminate this recursion process

3. Recursion is an amazing technique with the help of which we can reduce the length of our code and make it easier to read and
write. It has certain advantages over the iteration technique which will be discussed later. A task that can be
defined with its similar subtask, recursion is one of the best solutions for it

Algorithms:

1. Recursion is an amazing technique with the help of which we can reduce the length of our code and make it easier
to read and write. It has certain advantages over the iteration technique which will be discussed later. A task that
can be defined with its similar subtask, recursion is one of the best solutions for it

2. In every step, we try smaller inputs to make the problem smaller.
3. Base condition is needed to stop the recursion otherwise
infinite loop will occur.

Steps:

Step1 - Define a base case: Identify the simplest case for which the solution is known or trivial. This is the
stopping condition for the recursion, as it prevents the function from infinitely calling itself.


Step2 - Define a recursive case: Define the problem in terms of smaller sub problems. Break the problem down into
smaller versions of itself, and call the function recursively to solve each sub problem.

Step3 - Ensure the recursion terminates: Make sure that the recursive function eventually reaches the base case,
and does not enter an infinite loop.

step4 - Combine the solutions: Combine the solutions of the subproblems to solve the original problem.


Stored in the memory:
1. recursion uses more memory

What is the difference between direct and indirect recursion?

direct recursion: A function 'fn()' will always be call "fn()" with another parameter
indirect recursion: If it calls another function say func_new and fun_new call fn() directly or indirectly


tailed recursion: A recursive function is tail recursive when a recursive call is the last thing executed by the function

recursion:
1. Terminates when the base cse becomes true
2. used with functions
3. Every recursive call needs extra space in the stack memory
4. Smaller code size

Iteration
1. Terminates when condition becomes false
2. Used with loops
3. does not require any extra space.
4. Larger code size.

Real examples on recursion
1. Tree and Graph Traversal
2. Sorting algorithms
3. Divide and conquer algorithms
4. Fractal generation
5. Backtracking algorithms : technique which involves making o sequence of decisions where each decision depends on the previous one.
6. Memoization - techniques which stores the results of expensive function calls and returning the cached result when the same inputs occur again.
   It can be implemented using recursive functions to compute and cache the results of subproblems.
"""
