'''
https://www.youtube.com/watch?v=-IFmgue8sF0
https://practice.geeksforgeeks.org/problems/stock-span-problem-1587115621/1?page=1&company[]=Samsung&category[]=Arrays&sortBy=difficulty
in this problem, we have an price of stock in each day, and need to find the span of stock at day i.
Span_i : maximum no of consecutive day where the price <= price at day i
condition: at i =0 th day span_i =0

example (Stock price at day i): [100, 80, 60, 70, 60, 75, 85]
span_i: [1, 1, 1, 2, 1, 4, 6]
day: [0,1, 2, 3, 4, 5,6]
explaination:
1: 100 (day 0 so, It needs to have 1)
1: at day 1 price is 80 and smaller than 100 so, It does not satisfy the condition." bcz maximum no of consecutive day where the price < price at day i"
   bcz the price at current day i should be higher than previous days.
1: at day 2 price is 60 which is lesser than previous days
2: at day 3, price is 70 is greater than previous days so, [day 2+ day3] = 2 days, so span is 2
1: at day 4, price is 60 which is lesser than previous day so, it is 1
4: at day 5, price is 75 which is greater than 60(day4's price), 70(day 3's price), 60(day 2's price) = 3 days + current day = 4
6: at day 6, orice is 85 which gretaer than 75, 60, 70, 60, 80 = 5+1 days.

approach: It can be solve using array recursively finding the elements. but It would be O(N2) but expected time is O(N)
so, we can use Stack data structure to store the days and work with it. deque in python.
catch: stack will store the days for calculating the span.
'''
from collections import deque


def calculateSpan(a, n):
    '''
    @param a:
    @param n:
    @return:
    '''
    d = deque()  # it bahaves like stack in python
    d.append(0)  # appending 0th day
    s = [0] * n  # Span
    s[0] = 1  # initialising for 0th day
    for i in range(1, n):
        if a[i] < a[i - 1]:
            d.append(i)  # appending the days
            s[i] = 1
        if a[i] >= a[i - 1]:  # this will calculate the span
            while (len(d) > 0):
                no_of_day_from_stack = d[-1]
                if a[no_of_day_from_stack] <= a[i]:
                    d.pop()
                    continue
                else:
                    s[i] = i - d[-1]
                    d.append(i)
                    break
            if len(d) == 0:
                s[i] = i + 1
    print(s)


a = [100, 80, 60, 60, 70, 60, 75, 85]
# a =  [10, 4, 5, 90, 120,80]
n = len(a)

calculateSpan(a, n)
