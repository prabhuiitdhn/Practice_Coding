'''
in the problem statement, we need to find the next larger element for each element in the array from any array.
 If not existing the -1

 example:[6, 8, 0, 1, 3]
        [6->8, 8->-1, 0->1, 1->3, 3->-1]

'''

from collections import deque


# deque work on stack data structure.
#
#
# s = deque(maxlen=10) # initialise the deque with maxlen =10
# s.append(1) # appending is for appending the value in the stack
# s.append(2)
# s.append(3)
# s.pop()  # only pop() function is used for poping out the first element in the stack
# s.append(4)
# s.insert(0, 5)  # it is for adding the element in the index , 0th index with value 5.
# print(s)


'''
https://www.youtube.com/watch?v=uFso48YRRao
https://practice.geeksforgeeks.org/problems/next-larger-element-1587115620/1
    vector<long long> nextLargerElement(vector<long long> arr, int n){
        vector<long long> v(n, -1);
        stack<long long> s;
        for(int i=n-1; i >= 0; --i) {
            while( !s.empty() && s.top() <= arr[i] )
                s.pop();
            if(!s.empty())
                v[i] = s.top();
            s.push(arr[i]);
        }
        return v;
    }
'''


# This needs to change and modified.
def nextLargesNumberInarray(arr, n):
    l = [-1] * n
    s = deque(maxlen=n)

    for i in range(n):
        while (len(s) > 0 and s[0] <= arr[i]):
                s.pop()
                l[i - 1] = arr[i]
        if len(s)>0:
            l[i-1] = s.pop()

    return l


arr = [6, 8, 0, 1, 3]
print(nextLargesNumberInarray(arr, 5))
