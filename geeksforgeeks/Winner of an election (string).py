'''
https://practice.geeksforgeeks.org/problems/winner-of-an-election-where-votes-are-represented-as-candidate-names-1587115621/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Qualcomm&category[]=Strings&sortBy=difficulty
problem:
given the name of candidates in an array. Find the name which occurs maximum time, If tie then smaller no of char will win the election/name
approach: dictionary

input: arr= elements in array which takes the names in voting list
'''

import numpy as np
def winner2(arr, n):
    winner = {}

    for i in arr:

        if i not in winner:

            winner[i] = 1

        else:

            winner[i] += 1

    majority = 0

    for k, v in winner.items():

        if v > -1:
            majority = max(majority, v)

    m = max(sorted(winner), key=winner.get)

    return (m, majority)

def winner(arr, n):
    # Your code here
    # put the name and no of times it is being voted in Dictionary
    d = {}
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]] = 1
        else:
            d[arr[i]] = d[arr[i]] + 1

    max = -9999
    same_value = []
    # this will help to get the maximum votes at first.
    sorted_values = sorted(list(d.values()))[::-1]
    for i in range(len(sorted_values)):
        # choosing maximum time of number is being called in dictionary
        if max < sorted_values[i]:
            max = sorted_values[i]
            for key in d.keys():
                if d[key] == sorted_values[i]:
                    same_value.append(key)
                    d[key] = 0 # once one name is being added in same_value, next time this should not come so, value of this is making 0
                    break
            # same_value.append()
        elif max == sorted_values[i]:
            # this is for another name which comes as same time
            for key in d.keys():
                if d[key] == sorted_values[i]:
                    same_value.append(key)
                    d[key] = 0
                    break
        else:
            max = max

    # same_value contains the name which have the same value/no of votings
    winner_name = min(same_value) #it find the name which is lexicographically smaller. same_value is list of string.

    return (winner_name, max)

a = ["john", "johnny", "jackie",  "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny",  "jamie",  "johnny", "john"]
name, time_of_voting = winner(a, len(a))
print(name, time_of_voting)
