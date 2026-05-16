"""
https://practice.geeksforgeeks.org/problems/wildcard-pattern-matching/1?page=3&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
It is about given a pattern with * and ? and string
we needed to check whether the pattern is matching with string or not?
NOTE:
    * will take multiple sequence of character.
    ? will take single character.
    * can also be used for empty spaces
example:
 pattern = "ba*a?"
 string = "baaabab"
 in this example If we replace * with 'aab' and ? with 'b' then both pattern and string will match.

 So, many possiblities will come

pattern: ***aab**a?
string: aaabbaabaaacad
in this example: If *** will replace by aaabb and ** will aaaca and ? with d then both will match.




"""


def wildCard(pattern, string):
    """
    To make this work we have to take care of memoisation [Dynamic programming ] concepts which can help to keep
    already calculated in the buffer.
    """
    # Code here
    dp = {}

    def helper(pattern_index, string_index):
        if pattern_index == len(pattern) and string_index == len(string):
            # check if patten_index is already finished and string_index is already reached to last of the index.
            # return True bcz it is coming at the end after processing from starts/
            return True
        if pattern_index == len(pattern):
            # if pattern_index reached to end but string_index did not then We still have string character available
            # but not pattern available.
            return False
        if string_index == len(string): # CONDITION 3
            # this is the case where string index is reached to end but pattern_index is still remain so it will
            # check until it reached to end and If it is * and it can pass to next index bcz * can also work with
            # empty spaces.

            if pattern[pattern_index] == "*":
                while pattern_index < len(pattern) and pattern[pattern_index] == "*":
                    pattern_index += 1
                if pattern_index == len(pattern):
                    return True
                else:
                    return False
            else:
                return False

        if (pattern_index, string_index) in dp: return dp[(pattern_index, string_index)]
        if pattern[pattern_index] != string[string_index]:
            # this is the case when both index are into place but character are not matching apart from * and ?
            if pattern[pattern_index] != "*" and pattern[pattern_index] != "?":
                return False
            else:
                if pattern[pattern_index] == "*":
                    # it looks that If character is * and looks for next index for pattern and string and next for string and next for pattern to matching exceptional cases.
                    #(i, j) = (i+1, j+1) or (i+1, j) or (i, j+1)
                    dp[(pattern_index, string_index)] = helper(pattern_index + 1, string_index + 1) or helper(
                        pattern_index, string_index + 1) or helper(pattern_index + 1, string_index)
                else:
                    # this is case when will have '?' in the patern which can pass to next index.
                    dp[(pattern_index, string_index)] = helper(pattern_index + 1, string_index + 1)
        else:
            # this when string and pattern's character are matching.
            dp[(pattern_index, string_index)] = helper(pattern_index + 1, string_index + 1)
        return dp[(pattern_index, string_index)]

    return helper(0, 0)


# pattern = "ba*a?"
# string = "baaabab"

# pattern = "ba***a"
# string = "aa"

pattern = "*ccddee*"
string = "ccddee"

print(wildCard(pattern, string))
