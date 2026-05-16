"""
https://practice.geeksforgeeks.org/problems/8dcd25918295847b4ced54055eae35a8501181c1/1?page=3&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
SOLVE THE PROBLEM USING Z algorithm
https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/

"""




def search(string, pattern):
    list_ = []
    pattern_length = len(pattern)
    string_length = len(string)

    for i in range(string_length-pattern_length+1):
        if string[i:i+pattern_length] == pattern:
            list_.append(i+1)

    return list_



S = "batmanandrobinarebat"
pat = "bat"
print(search(S, pat))