"""
https://practice.geeksforgeeks.org/problems/ea8230731ccb057120bafb351c10c48b2d496125/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Greedy&sortBy=difficulty

Given N events in geek's city.
in the geek's city, for each events, starting and ending time is being given. so, Needed to find out the maximum no of events a person can attend.
& a person can attend one event at a time.

TO maximize the event which are already being attended is try to attend the last day, and If it is attended the last
and another events came then try to attend the 2nd last day of the same effect.

"""

from collections import deque


def maxEvents(start, end, n):
    """
    @param start: starting day of the events.
    @param end: Ending day of the events.
    @param N: total no of events.
    @return: no of maximum events one can attend.
    """

    # sorted the events which tell that what is maximum no of days which goes for events
    end_day_sorted = sorted(end)

    # this is for keep the track of which day is being attended or not
    max_day_of_event = end_day_sorted[-1]
    list_of_day = [0] * max_day_of_event

    list_of_events = deque()
    # to work with the different events which started on the same days
    for i in range(n):
        list_of_events.append([start[i], end[i]])

    list_of_events = sorted(list_of_events)

    while list_of_events:
        # pop the current events
        current_event = list_of_events.pop()
        if list_of_day[current_event[1] - 1] != -1:
            # to maximize the event attending try to attend by last day of the event
            # check whether if this event is being attended or not? If not then marked as attended.
            list_of_day[current_event[1] - 1] = -1
        else:
            for i in range(current_event[1], current_event[0] - 1, -1):
                # if the event is being attended on the last day then finding if can be attended the 2nd last day of the
                # event.
                if list_of_day[i - 1] != -1:
                    list_of_day[i - 1] = -1
                    break

    count_event = 0

    for i in range(len(list_of_day)):
        # Counting the no of events which are attended.
        if list_of_day[i] == -1:
            count_event += 1

    return count_event


# start = [1, 1, 1, 2, 2, 2, 3, 3, 4]
# end = [1, 2, 3, 2, 3, 4, 6, 3, 4]
# n = 9
#
start = [5, 10, 1, 2, 4, 1, 1, 1, 1]
end = [5, 10, 2, 7, 9, 3, 3, 1, 5]
n = 9

# n = 7
# start = [1, 1, 1, 6, 7, 3, 8]
# end = [1, 8, 4, 6, 7, 5, 8]
print(maxEvents(start, end, n))
