"""
This is about checking the valid sudoko.
where number should be [1-9]
1. Each row should contain only one value between [1-9]
2. Each column should contain one value between [1-9]
3. Each 3x3 block should contain only one value between [1-9]

if value is not present then okay but should not contain same number more than once.
if this happen, it is not valid sudo.
"""
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for row in range(9):
            # checking each row If the frequency of value is less than 2 or not.
            d = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
            for j in range(9):
                if board[row][j] != ".":
                    d[board[row][j]] += 1

                for value in d.values():
                    if value > 1:
                        return False

        for col in range(9):
            # check each column if the frequency of the value is less than 2
            d = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
            for j in range(9):
                if board[j][col] != '.':
                    d[board[j][col]] += 1
                for value in d.values():
                    if value > 1:
                        return False
        num = 3
        for i in range(3):
            # It is checking each 3x3 block if the frequency of value is less than 2 or not.
            for l in range(3):
                start_index = num * i
                end_index = num * (i + 1)
                d = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
                for p in range(start_index, end_index):
                    start_k = num * l
                    end_k = num * (l + 1)
                    for k in range(start_k, end_k):
                        if board[p][k] != ".":
                            d[board[p][k]] += 1
                for value in d.values():
                    if value > 1:
                        return False


        return True


#
# board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
#     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
#     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
#     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
#     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
#     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
#     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
#     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
#     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

# board = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

board = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]

print(len(board[0]))
s = Solution()
print(s.isValidSudoku(board))
