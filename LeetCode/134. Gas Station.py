"""
https://leetcode.com/problems/gas-station/solutions/1004074/greedy-method-explanation-visual-python/ [One of the best explanation ]

"""

class Solution(object):
    def canCompleteCircuit2(self, gas, cost):
        # THIS IS WORKING BUT NEEDED TO OPTIMISE IT.
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_index = len(gas)

        def process_and_check(index):
            filled_up = gas[index % total_index]  # filled in the station
            required = cost[index % total_index]
            next_station_index = (index + 1) % total_index
            filled_up_next_station = gas[next_station_index]
            remaining = filled_up - required + filled_up_next_station  # still remaining
            if remaining < cost[next_station_index]:
                return False
            for _index in range(index + 1, index + total_index):
                current_index = _index % total_index
                filled_up = remaining  # filled in the station
                required = cost[current_index]  # needed to cost this for travelling
                next_station_index = (current_index + 1) % total_index
                filled_up_next_station = gas[next_station_index]
                remaining = filled_up - required + filled_up_next_station  # still remaining
                if remaining < cost[next_station_index]:
                    return False

            return True

        for i in range(total_index):
            filled_up = gas[i]
            required_gas = cost[i]
            if filled_up < required_gas:
                continue
            else:
                if process_and_check(i):
                    return i
                else:
                    continue
        return -1


    def canCompleteCircuit(self, gas, cost):
        # USING GREEDY APPROACH
        # WORKED FINE.
        trip_tank = 0 # IT KEEP THE INFORMATION OF FUEL TILL THE END OF THE TRIP
        current_tank = 0 # THIS TAKES CARE OF CURRENT TRIP, IF IT IS LESS THAN 0 then WE should look for new trip points[starting point.]
        start = 0
        for i in range(len(gas)):
            trip_tank += gas[i] - cost[i]
            current_tank += gas[i]- cost[i]
            if current_tank<0:
                start = i+1
                current_tank =0
        if trip_tank>=0:
            return start
        else:
            return -1


gas = [2, 3, 4]
cost = [3, 4, 3]

# gas = [1,2,3,4,5]
# cost = [3,4,5,1,2]

# gas = [5, 1, 2, 3, 4]
# cost = [4, 4, 1, 5, 1]

s = Solution()
print(s.canCompleteCircuit(gas, cost))
