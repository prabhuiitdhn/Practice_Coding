"""
https://practice.geeksforgeeks.org/problems/word-search/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Recursion&sortBy=difficulty

given the words and board, needed to check whether the word is being found in the board or not?
check if the given word is being found in the given board.

approach: recursion.
"""


# class Solution:
#     # def __init__(self):
#     #     self.result = 0
#
#     def helper(self, r, c, rows, cols, board, indexofword, word):
#         # left, right, top, bottom
#         positionList = [(0, -1), (0, 1), (-1, 0), (1, 0)]
#         if indexofword == len(word) - 1:
#             self.result =1
#             return
#
#         # adding the visited node.
#         temp = board[r][c]
#         board[r][c] = -1
#
#         for pos in positionList:
#             r = r + pos[0]
#             c = c + pos[1]
#             if 0 <= r < rows and 0 <= c < cols and board[r][c] == word[indexofword + 1]:
#                 self.helper(r, c, rows, cols, board, indexofword + 1, word)
#             r -= pos[0]
#             c -= pos[1]
#         board[r][c] = temp
#
#     def isWordExist(self, board, word):
#         self.result = 0
#         index_of_word = 0
#         rows = len(board)
#         cols = len(board[0])
#         for i in range(rows):
#             for j in range(cols):
#                 if board[i][j] == word[0]:
#                     self.helper(i, j, rows, cols, board, index_of_word, word)
#                     if self.result == 1:
#                         return True
#
#         return False

class Solution:
    # def __init__(self):
    #     self.result = 0

    def helper(self, r, c, rows, cols, board, word):
        # left, right, top, bottom
        positionList = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        if len(word) == 0:
            # this keeps track of the result.
            # if in the recursion word found in the board then It keeps the information that word is being found.
            self.result =1
            return

        # adding the visited node.
        temp = board[r][c]
        # used for marked as visited node.
        board[r][c] = -1

        for pos in positionList:
            # from the index it starts looking for all four possible possible from the index.
            r = r + pos[0]
            c = c + pos[1]
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == word[0]:
                # check If the starting word from the remaining work is being found or not?
                # if yes, then It starts again looking for next word.
                self.helper(r, c, rows, cols, board, word[1:])

            # this is the case when no matching letter found on the four side.
            # It gets back to previous position If no next letter is being found.
            r -= pos[0]
            c -= pos[1]

        # It keeps back the letter in the board If not found anything from that index.
        board[r][c] = temp

    def isWordExist(self, board, word):
        self.result = 0
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    # finding the starting index where the first letter of word is being found, If found then it send
                    # to helper which looks four side from that index and look for next letter in the work.
                    # It also keeps track of the letter/index which is already visited.
                    self.helper(i, j, rows, cols, board, word[1:])
                    if self.result == 1:
                        return True

        return False


# board = [['a', 'g', 'b', 'c'],
#          ['q', 'e', 'e', 'l'],
#          ['g', 'b', 'k', 's']]
# word = 'geeks'

board = [['a', 'b', 'c', 'e'],
         ['s', 'f', 'c', 's'],
         ['a', 'd', 'e', 'e']
         ]
word = "sabfs"

s = Solution()
print(s.isWordExist(board, word))
