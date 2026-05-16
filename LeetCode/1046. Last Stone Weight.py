class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            index_x = stones.index(max(stones))
            max_x = max(stones)
            temp = -9999
            stones[index_x] = temp
            index_y = stones.index(max(stones))
            max_y = max(stones)
            stones[index_x] = max_x
            if max_x == max_y:
                stones[index_x] = -999999
                stones[index_y] = -999999
                stones.remove(-999999)
                stones.remove(-999999)
            else:
                weight = max_x - max_y
                stones[index_x] = weight
                del stones[index_y]

        if len(stones) > 0:
            return stones[0]
        else:
            return 0
