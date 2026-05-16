"""
https://practice.geeksforgeeks.org/problems/count-palindrome-sub-strings-of-a-string0652/1?page=2&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
Input
N = 5
str = "abaab"
Output
3
Explanation:
All palindrome substring are : "aba" , "aa" , "baab"

"""


def countPS(str, N):
    """
    Basic Native approach
    @param str:
    @param N:
    @return:
    """
    count = 0
    for length in range(2, N + 1):  # started working through length of window
        for window in range(N - length + 1):
            # this starts indexing where str should be taken for comparison.
            currentStr = str[window:window + length]
            if currentStr == currentStr[::-1]:
                count += 1

    return count


def countPSDPRecursive(str, N):
    def helper(str, start, end):
        if start == end:
            dp[start][end] = 1

        if start + 1 == end and str[start] == str[end]:
            dp[start][end] = 2
        if dp[start][end] == -1:
            if str[start] == str[end]:
                a = 2 + helper(str, start + 1, end - 1)
                b = helper(str, start + 1, end)
                c = helper(str, start, end - 1)
                dp[start][end] = max(a, b, c)
            else:
                a = helper(str, start + 1, end)
                b = helper(str, start, end - 1)
                dp[start][end] = max(a, b)
        return dp[start][end]

    dp = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]
    helper(str, 0, N - 1)
    answer = 0
    for i in range(N + 1):
        for j in range(i + 1, N + 1):
            if j - i + 1 == dp[i][j]:
                answer += 1
    return answer


def countPSDPIterative(str, N):
    """
    It fails to pass all the test cases.
    @param str:
    @param N:
    @return:
    """
    dp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][i] = 1

    for i in range(N - 1):
        if str[i] == str[i + 1]:
            dp[i][i + 1] = 1

    for j in range(2, N):
        for i in range(N - j):
            left = i
            right = i + j
            if (str[left] == str[right]) and dp[left + 1][right - 1]:
                dp[left][right] = 1

    count = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j]:
                count += 1

    return count - N


def countPSDPIterative2(str, N): # passed the test cases
    """
    So basically we started counting iteratively that how many
    @param str:
    @param N:
    @return:
    """
    count = 0
    dp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        # this is for diagonal elements
        dp[i][i] = 1

    for j in range(N - 1):
        if str[j] == str[j + 1]:
            dp[j][j + 1] = 1
            count +=1

    for gap in range(2, N):
        for n in range(N - gap):
            if str[n] == str[n + gap] and dp[n+1][n+gap-1]:
                dp[n][n + gap] = 1
                count += 1

    return count



str = "abaab"
# str = "aaaaa"
# str = "abbaeae"
N = len(str)
# print(countPS(str, N))
# print(countPSDPRecursive(str, N))
# print(countPSDPIterative(str, N))
print(countPSDPIterative2(str, N))
