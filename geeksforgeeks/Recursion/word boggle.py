"""
https://practice.geeksforgeeks.org/problems/word-boggle4143/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Recursion&sortBy=difficulty

This problem is give a list of word in the dictionary and board where letter are presents.
so, Needs to find out all the letter which is being found in the board.
Possibilities with all direction from the index. [top, bottom, left, right, 4 diagonals.]

condition:
 A cell can be used only once in one word.

"""


class Solution2:
    """
    this is based on recursion but it needed to optimise it. It taking lot of time to execute for higher number of inputs
    It works for all the cases but Needed to optimise the code in larger length of word size or board size.
    """

    def __init__(self):
        self.result = 0
        self.dp = []

    def helper(self, r, c, rows, cols, board, indexofword, word):
        # left, right, top, bottom
        positionList = [[-1, 0], [1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]
        if indexofword == len(word) - 1:
            self.result = 1
            return

        # adding the visited node.
        temp = board[r][c]
        board[r][c] = -1

        for pos in positionList:
            r = r + pos[0]
            c = c + pos[1]
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == word[indexofword + 1]:
                self.helper(r, c, rows, cols, board, indexofword + 1, word)
            r -= pos[0]
            c -= pos[1]
        board[r][c] = temp

    def wordBoggle(self, board, dictionary):
        finalList = []
        rows = len(board)
        cols = len(board[0])
        stop = False

        for word in dictionary:
            self.result = 0
            stop = False

            for r in range(rows):
                for c in range(cols):
                    if board[r][c] == word[0] and stop is False:
                        self.helper(r, c, rows, cols, board, 0, word)
                        if self.result == 1:
                            finalList.append(word)
                            stop = True

        return finalList



class Solution:
    """
    This is improved code which used for all the cases.
    """

    def find(self, board, word):

        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]

        def dfs(r, c, pos):
            if pos == len(word):
                return True
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and visited[r][c] == False and board[r][c] == \
                    word[pos]:
                visited[r][c] = True
                if (dfs(r + 1, c, pos + 1)
                        or dfs(r, c + 1, pos + 1)
                        or dfs(r - 1, c, pos + 1)
                        or dfs(r, c - 1, pos + 1)
                        or dfs(r + 1, c + 1, pos + 1)
                        or dfs(r + 1, c - 1, pos + 1)
                        or dfs(r - 1, c + 1, pos + 1)
                        or dfs(r - 1, c - 1, pos + 1)):
                    return True
                # to check that the character can be used in another word
                visited[r][c] = False

            return False

        indx = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[indx]:
                    if dfs(i, j, indx):
                        return True
        return False

    def wordBoggle(self, board, dictionary):
        res = []
        for i in range(len(dictionary)):
            word = dictionary[i]
            if self.find(board, word):
                res.append(word)
        return res


# dictionary = ["CAT"]
# board = [['C', 'A', 'P'],
#          ['A', 'N', 'D'],
#          ['T', 'I', 'E']]

#
# dictionary = ["GEEKS","FOR","QUIZ","GO"]
# board = [['G','I','Z'],['U','E','K'],['Q','S','E']]
#
#
dictionary = ["bcd", "db"]
board = [['d', 'd'],
         ['b', 'f'],
         ['e', 'c'],
         ['b', 'c'],
         ['d', 'c']]
s = Solution3()
p = s.wordBoggle(board, dictionary)
print(p)
