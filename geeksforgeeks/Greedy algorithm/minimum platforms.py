"""
https://www.youtube.com/watch?v=dxVcMDI7vyI
https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Greedy&sortBy=difficulty

problem:
given an arrival and departure time of the train, needed to find out the minimum no of platforms required for all the train in a day
condition: if the arrival time of one train, and departure time of another train is same then it required to have another platform to work with it.

solution: It can be used using greedy algorithm which only take care about the current optimal solution without thinking the future of it.
approach:
1. sort the arrival time and departure time

2. compare the arrival time with departure time, If arrival time < last stored departure time then new platform is
needed bcz if current train is not departed then not new train can arrive to the plaform and if arrival time > last
store departure time then no need to have new platform to be added. remove the required platform until arrival <
departure time. """


def minimumPlatform(n, arr, dep):
    """
    @param n: represents the numbers train.
    @param arr: array in arrival time
    @param dep: departure time of thr trains
    @return: no of platforms required for all the train so that no train has to wait.
    """
    arrival = sorted(arr)
    departure = sorted(dep)
    max_platform = 1
    platformRequired = 1
    arrival_index, departure_index = 1, 0
    while arrival_index < n and departure_index < n:
        if arrival[arrival_index] > departure[departure_index]:
            platformRequired -= 1
            max_platform = max(max_platform, platformRequired)
            departure_index += 1
        else:
            platformRequired += 1
            max_platform = max(max_platform, platformRequired)
            arrival_index += 1

    return max_platform


# total num of train's times which will arrive and departs
n = 6
# arrival time of the trains
arr = [900, 940, 950, 1100, 1500, 1800]
# departure time of the trains.
dep = [910, 1200, 1120, 1130, 1900, 2000]

print("Minimum no of platform required:", minimumPlatform(n, arr, dep))
