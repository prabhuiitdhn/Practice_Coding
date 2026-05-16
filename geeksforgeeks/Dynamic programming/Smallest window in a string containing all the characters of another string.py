"""
https://practice.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1?page=5&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=PayPal&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

Asked in google. Please clear the concpets.
"""

# PLEASE WORK ON BY YOURSELF. THIS IS SO IMPORTANT QUESTION
def smallestWindow(string, pattern):
    if pattern == "":
        # This is for when pattern is empty string the return empty
        return ""
    countT, window = {}, {}
    # countT is for keeping the alphabets in dictionary
    # window
    for c in pattern:
        countT[c] = countT.get(c, 0) + 1
    have, need = 0, len(countT)
    result = [-1, -1]
    resLen = float("infinity")
    l = 0
    for r in range(len(string)):
        c = string[r]
        window[c] = window.get(c, 0) + 1
        if c in countT and window[c] == countT[c]:
            have += 1
        while have == need:
            if (r - l + 1) < resLen:
                result = [l, r]
                resLen = (r - l + 1)
            window[string[l]] -= 1
            if string[l] in countT and window[string[l]] < countT[string[l]]:
                have -= 1
            l += 1
    l, r = result
    return string[l:r + 1] if resLen != float("infinity") else "-1"


string: str = "timetopractice"
pattern: str = "toc"
print(smallestWindow(string, pattern))
