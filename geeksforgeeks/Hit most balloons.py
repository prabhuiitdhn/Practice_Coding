"""
https://practice.geeksforgeeks.org/problems/hit-most-balloons--170637/1?page=1&difficulty[]=1&company[]=PayPal&company[]=Nvidia&company[]=KLA%20Tencor&sortBy=difficulty

Given an infinite 2D matrix, we do have balloon kept in any grid of this 2d matrix.
I have an arrow to shoot the balloon, how many maximum balloons we can shoot at one shot.
starting point of shooting, can be anywhere and target can also be anywhere.

thought: If we start shooting balloons then arrow should be in one direction to have maximum balloon burst. Also, from the starting point of balloon should have 8 possible way to shoot the arrow for the next balloons
So ultimately the balloon should in a line. so needed to check the maximum balloon which lies in a line.
Now, to find the maximum balloons in the line, we need to calculate the slope and for this slope, check how many balloon are in the lines.
"""


def mostBalloons(N, arr):
    ans = 0 # it keeps the value of maximum point lies in the line.

    for i in range(N - 1): # from 1st point to last-to last point to comapre with last point.
        # comparing each points to remaining points and check how many balloons we have in the same line.
        current_count = 1
        dict = {}  # put the dictionary and key as slope and value as number of points.
        for j in range(i + 1, N): # remaining points to find out the slopes.
            # condition for points are same
            if arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1]:
                # It checks If the points are same
                current_count += 1
                continue
            # handle division by 0
            # to calculate the slope we need to have numerator and denominator.
            numerator = (arr[j][1] - arr[i][1])
            denominator = (arr[j][0] - arr[i][0])
            if numerator == 0:
                # trying to divide 0/number = 0.0
                slope = 0.0
            elif denominator == 0.0:
                # but if number/0.0 is not divisible so slope is infinite.
                slope = 10 ** 9 + 1
            else:
                slope = numerator / denominator

            # keeping how many points lies in the calculated slope.
            dict[slope] = dict.get(slope, 0) + 1

        for value in dict.values():
            ans = max(ans, value + current_count)

    return ans


N = 3
arr = [[1, 2], [2, 3], [3, 4]]


print(mostBalloons(N, arr))
