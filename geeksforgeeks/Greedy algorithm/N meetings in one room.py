"""https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1?page=1&company[]=Amazon&company[
]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[
]=Greedy&sortBy=difficulty


problem: If starting and ending time is being given in unsorted order then check in a
given time how many meetings can be arranged in one meeting room

Solution:
1. using two pointer approach, keep track of current, and prev pointer. and track them based on condition
2. using stack this can be solved.
"""


def maximumMeetings(start, end, n):
    count = 1
    i = 1  # next index
    j = 0  # previous index

    list_of_meeting_times = []
    for index in range(n):
        list_of_meeting_times.append([start[index], end[index]])

    # Sorting the meeting time by the end times.
    list_of_meeting_times = sorted(list_of_meeting_times, key=lambda l: l[1])

    while i < n and j < n:
        if list_of_meeting_times[i][0] > list_of_meeting_times[j][1] and list_of_meeting_times[i][0] > \
                list_of_meeting_times[j][0]:

            # Checking if starting time of current index > ending index of prev index
            # and if starting time of current index > starting index of prev index
            # if this is tru then count,  current will become previous and i will increase by 1
            count += 1
            j = i
            i += 1
        else:
            # if not satisfied then only current index will increase to cross check with previous
            i += 1

    return count


start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
n = 6

# n = 8
# start = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
# end = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
print(maximumMeetings(start, end, n))
