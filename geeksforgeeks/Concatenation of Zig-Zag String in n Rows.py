"""
https://practice.geeksforgeeks.org/problems/concatenation-of-zig-zag-string-in-n-rows0308/1?page=1&difficulty[]=1&company[]=PayPal&company[]=Nvidia&company[]=KLA%20Tencor&sortBy=difficulty

So basically this is about how to write the Given string in zig-zag fashion.

example: ABCDEFGH
rows=2

A       C       E       G       row:1
    B       D       F       H   row:2

final output: ACEGBDFH

time complexity = O(|str|)

Approach: down flag which is False until It reaches to last row, after reaching to the last row Down = True [reached to down]
        again It will be True until it reaches to top row.
        Track is for tracking the row number.

https://www.youtube.com/watch?v=LhacuzXRVKI&ab_channel=GeeksforGeeks
"""


def convert(input_str, rows):
    output_string = [''] * rows  # For each rows we need to have sting which can only add that row string value.
    down = False  # Flag for tracking to the last row or not?
    track = 0  # this keeps track of last row.

    for ch in input_str:  # Iterating each element in the string.
        if down is False and track < rows:
            # check If it is not reached to last row and track is less than rows
            output_string[track] += ch  # add character of string into the output_string index.
            track += 1
            # continue

        if down is False and track == rows:
            # if track passed to last row
            down = True
            track -= 2  # bcz we have to go 2 step up for second last row. bcz track increased to rows
            continue

        if down is True and track > -1:
            output_string[track] += ch
            track -= 1
            # continue

        if track == -1 and down is True:
            down = False
            track += 2  # track decreased to -1 so, reach first 2 rows needed to add 2
            continue

    converted_output_str = ""
    for j in range(rows):
        converted_output_str += output_string[j]

    return converted_output_str


# str = "ABCDEFGH"
str = "GEEKSFORGEEKS"
n = 3
print(convert(str, n))
