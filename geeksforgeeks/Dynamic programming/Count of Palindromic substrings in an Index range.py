"""
https://practice.geeksforgeeks.org/problems/count-of-palindromic-substrings-in-an-index-range3752/1?page=2&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
"""
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
        count +=1

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

str = "xyaabax"
q1 = 3
q2 = 5
if q1>q2:
    q1, q2 = q2, q1
cropped_str = str[q1:q2+1]
len_of_cropped_str = len(cropped_str)
print(countPSDPIterative2(cropped_str, len_of_cropped_str))
