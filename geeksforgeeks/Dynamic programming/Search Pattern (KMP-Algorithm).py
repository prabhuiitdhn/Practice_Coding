"""
PLEASE IMPLEMENT IT FROM SCRATCH
problem:https://practice.geeksforgeeks.org/problems/search-pattern0205/1?page=3&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
YouTube:https://www.youtube.com/watch?v=ziteu2FpYsA
GeeksforGeeks: https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/?ref=lbp

So basically, We will be given string and pattern which needs to find whether the pattern is found in the string or not?
example:
string = "batmanandrobinarebat"
pattern = "bat"
Using the searching algorithm, we can see that Index 0, and 18 where we can look for pattern.

Approach: We will create a lps(Largest prefix in patter which is same as suffix)
example:
pattern: abcaby
LPS:[0, 0, 0, 1, 2, 0] where lps[i] says: How many character in the pattern which have prefix as well as suffix
lps[0]: only one character is 'a'
lps[1]: only common characters are present no repeated, 'a', 'b'
lps[2]: still only common character are present
lps[3]: 'a' are the only character which repeats 'abca' in this pattern we have largest prefix is 'a' which having the same suffix 'a'
lps[4]: 'ab' are the character which are repeated 'abcab' in this pattern we have largest prefix is ab
lps[5]: again abcaby; 'y' is unique here so it is 0

The only reason of doing this is to search in such a way that we don't have to from starting index of pattern if character is not matching in string. It helps to keep track that how many
character are already matched in pattern in string until the current index.

"""


# User function Template for python3
class Solution:
    # code here
    def search(self, pattern, string):
        def longest_prefix_suffix_pattern(pattern):
            pattern_length = len(pattern)
            pattern_list = [0] * pattern_length

            i = 0
            j = 1
            while i < pattern_length and j < pattern_length:
                if pattern[i] != pattern[j]:
                    if i != 0:
                        pattern_list[j] = pattern_list[i - 1]
                    else:
                        pattern_list[j] = 0
                    j += 1
                else:
                    pattern_list[j] = i + 1
                    j += 1
                    i += 1

            return pattern_list

        string_length = len(string)
        pattern_length = len(pattern)
        index_list = []
        lps_list = longest_prefix_suffix_pattern(pattern)
        # print("lps_list:", lps_list)

        current_pattern_index = 0
        current_string_index = 0

        while current_string_index < string_length:
            if string[current_string_index] == pattern[current_pattern_index]:
                current_pattern_index += 1
                current_string_index += 1
            else:
                current_pattern_index = lps_list[current_pattern_index - 1]
                if current_pattern_index == 0:  # the first element
                    current_string_index += 1
            if current_pattern_index == pattern_length:
                index_list.append(current_string_index - current_pattern_index + 1)
                current_pattern_index = 0
                current_string_index = current_string_index - 1

        return index_list


# string: str = "abxabcabcaby"
# pattern: str = "abcaby"
#
# string: str = "batmanandrobinarebat"
# pattern: str = "bat"

string: str = "aaaaaa"
pattern: str = "aa"
# print(longest_prefix_suffix_pattern(pattern))
s = Solution()
print("Matched Indices:", s.search(pattern, string))
