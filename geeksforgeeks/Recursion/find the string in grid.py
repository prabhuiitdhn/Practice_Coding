"""
https://practice.geeksforgeeks.org/problems/find-the-string-in-grid0111/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Recursion&sortBy=difficulty
problem: given a 2D grid of n*m characters and word, so needed to find all occurence of given words in the grid and a word can be matched to all the 8 directions at any points.
return: index where the word started matching.


"""

from typing import List


def searchWord3(grid, word) -> List:
    """
    this is the case when direction needs to be corrected.
    Also, this also consider the visited node.
    @param grid:
    @param word:
    @return:
    """
    l = []
    n = len(grid)  # rows
    m = len(grid[0])  # columns
    found = False

    def _helper(grid, word, index_i, index_j):
        if word is '':
            return True

        while index_i < n and index_j < m:
            if 0 <= index_i + 1 < n and 0 <= index_j + 1 < m:
                if grid[index_i + 1][index_j + 1] == word[0]:
                    # RB diagonal this is for +ve diagonal
                    index_i = index_i + 1
                    index_j = index_j + 1

                    return _helper(grid, word[1:], index_i, index_j)

            if 0 <= index_i - 1 < n and 0 <= index_j - 1 < m:
                if grid[index_i - 1][index_j - 1] == word[0]:
                    # UL diagonal this is for -ve diagonal
                    index_i = index_i - 1
                    index_j = index_j - 1

                    return _helper(grid, word[1:], index_i, index_j)

            if 0 <= index_i + 1 < n and 0 <= index_j - 1 < m:
                if grid[index_i + 1][index_j - 1] == word[0]:
                    # LB diagonal
                    index_i = index_i + 1
                    index_j = index_j - 1

                    return _helper(grid, word[1:], index_i, index_j)

            if 0 <= index_i - 1 < n and 0 <= index_j + 1 < m:
                if grid[index_i - 1][index_j + 1] == word[0]:
                    # UR diagonal
                    index_i = index_i - 1
                    index_j = index_j + 1

                    return _helper(grid, word[1:], index_i, index_j)

            if 0 <= index_i - 1 < n and 0 <= index_j < m:
                if grid[index_i - 1][index_j] == word[0]:
                    # parallel top
                    index_i = index_i - 1
                    index_j = index_j - 1

                    return _helper(grid, word[1:], index_i, index_j)

            if 0 <= index_i + 1 < n and 0 <= index_j < m:
                if grid[index_i + 1][index_j] == word[0]:
                    # parallel down
                    index_i = index_i + 1
                    index_j = index_j

                    return _helper(grid, word[1:], index_i, index_j)

            if 0 <= index_i < n and 0 <= index_j - 1 < m:
                if grid[index_i][index_j - 1] == word[0]:
                    index_i = index_i
                    index_j = index_j - 1

                    return _helper(grid, word[1:], index_i, index_j)

            if 0 <= index_i < n and 0 <= index_j + 1 < m:
                if grid[index_i][index_j + 1] == word[0]:
                    index_i = index_i
                    index_j = index_j + 1
                    return _helper(grid, word[1:], index_i, index_j)

            break
        return False

    for i in range(n):
        for j in range(m):
            if grid[i][j] == word[0]:
                if len(word[1:]) > 1:
                    if _helper(grid, word[1:], i, j):
                        l.append([i, j])
    return l



def searchWord(board, word):
    """
    improved code. checks all the direction and same node would not be counted again and again.
    @param board:
    @param word:
    @return:
    """
    def help(board, w, r, c):
        x = [[-1, 0], [1, 0], [-1, 0],[0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

        if board[r][c] != w[0]:
            return False

        for i in x:
            rs = r + i[0]
            cs = c + i[1]
            Flag = True
            for k in range(1, len(w)):
                if (0 <= rs < len(board)) and (0 <= cs < len(board[0])) and w[k] == board[rs][cs]:
                    rs += i[0]
                    cs += i[1]
                else:
                    Flag = False
                    break

            if Flag:
                return True

        return False

    l = []
    rows = len(board)
    cols = len(board[0])

    for i in range(rows):
        for j in range(cols):
            if help(board, word, i, j):
                l.append([i, j])

    l.sort(key=lambda x: x[0])

    return l
#
#
# grid = [['a', 'b', 'c'], ['d', 'r', 'f'], ['g', 'h', 'i']]
# word = "abc"

# grid = [['a', 'b', 'a', 'b'],
#         ['a', 'b', 'e', 'b'],
#         ['e', 'b', 'e', 'b']]
# word = "abe"


# grid = ['c', 'b', 'a', 'c', 'e', 'a']
# word = "ead"


# grid = [['a', 'c'], ['c', 'e'], ['d', 'a'], ['c', 'd'], ['e', 'e'], ['a', 'a'], ['b', 'b'], ['d', 'a'], ['b', 'c']]
# word = "dcb"
#
grid = [['a', 'g', 'b', 'c'],
        ['q', 'e', 'e', 'l'],
        ['g', 'b', 'k', 's']]

word = "geeks"

list_ = searchWord(grid, word)
print(list_)
