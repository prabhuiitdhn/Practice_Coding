""""
DP is an optimisation problem, which works over the plain recursion. whenever repeated call for the same inputs.
simply store the results of the subproblems. so that this can be used later. This reduces the complexity from exponential to polynomial.

memoization: It is used for speed up computer program by elimination the repetative computation of results.
It basically stores the previously computed results of the subproblem and uses stored results for the same subproblem.
This removes the extra effort to calculate again and again for the same problem

if we store the result of subproblem which needs to be find out later then It would be find in O(1) time complexity.

this kind of problem is mostly used in the context of recursion
 "overlapping subproblems"/

type of memoization:
1. 1D memoisation: one parameter in the recursive function is variable
2. 2D memoisation: Two parameter in the recursive function is varaible
3. 3D memoisation: Three paramter in the recursive function is variable.

Dynamic programming helps to efficiently solve problems that have overlapping subproblems and optimal substructure properties. The idea behind dynamic programming is to break the problem into smaller sub-problems and save the result for future use, thus eliminating the need to compute the result repeatedly.

Two approach:
1. Top down approach: This approach follows the memoization technique. It consists of recursion and caching. In computation, recursion represents the process of calling functions repeatedly, whereas cache refers to the process of storing intermediate results
2. Bottom-up approach: This approach uses the tabulation technique to implement the dynamic programming solution. It addresses the same problems as before, but without recursion. In this approach, iteration replaces recursion. Hence, there is no stack overflow error or overhead of recursive procedures.

Applications:
1. Make a change problem
2. Knapsack problem
3. Optimal binary search

"""
"""
Tabulation VS Memoization
Tabulation: Bottom up
    Stores the results of subproblems in a table
    Iterative implementation    
    Well-suited for problems with a large set of inputs
    Used when the subproblems do not overlap

Memoization: Top down
    Caches the results of function calls
    Recursive implementation
    Well-suited for problems with a relatively small set of inputs
    Used when the subproblems have overlapping subproblems


Overlapping subproblems: When the solutions to the same subproblems are needed repetitively for solving the actual problem.
Optimal substructure property: If the optimal solution of the given problem can be obtained by using optimal solutions of its subproblems then the problem is said to have Optimal Substructure Property.

Memoization is a top-down approach where we cache the results of function calls and return the cached result if the function is called again with the same inputs. It is used when we can divide the problem into subproblems and the subproblems have overlapping subproblems. Memoization is typically implemented using recursion and is well-suited for problems that have a relatively small set of inputs.

Tabulation is a bottom-up approach where we store the results of the subproblems in a table and use these results to solve larger subproblems until we solve the entire problem. It is used when we can define the problem as a sequence of subproblems and the subproblems do not overlap. Tabulation is typically implemented using iteration and is well-suited for problems that have a large set of inputs.



"""
