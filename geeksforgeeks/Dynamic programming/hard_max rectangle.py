"""
https://practice.geeksforgeeks.org/problems/max-rectangle/1?page=5&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

Problem:
given a nXm matrix with 0s and 1s and needed to find out the maximum area contains in the matrix
given:
arr=  [
         [0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]
      ]

The largest area can be found from (1, 0) to (2, 3)
Expected Time Complexity : O(n*m)
Expected Auxiliary Space : O(m)

Approaches:
[this approach can be implemented using stack or datastructure.]
using the histogram: https://www.geeksforgeeks.org/maximum-size-rectangle-binary-sub-matrix-1s/
update each row with previous row: check in each row what is the maximum area can be found in each row

arr=  [
         [0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]
      ]
step1: [0, 1, 1, 0] maxarea: 1x2 = 2
step2= [1, 2, 2, 1] max area: 1x4 = 4 or 2x2 = 4
step3 = [2, 3, 3, 2] maxarea: 2x4 = 8
steps4: [3, 4, 0, 0 [bcz the current element is 0 so it will not come under the area]] = max area: 3x2

after that we have maximum area as 8

Using Dynamic programming.
https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
"""


