"""
https://practice.geeksforgeeks.org/problems/special-keyboard3018/1?page=2&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

this is one of most important question is being asked in google microsoft and all.
So, in this question. we do have given keys and Number of strokes i.e. this is maximum time we can press the key from the keyboard.
Key 1: print "A" on the screen
Key 2: ctrl + A; It is for selecting the text from the screen
key 3: ctrl + C; it is for copything the selected text in the screen
key 4: ctrl + v: it is for pasting the copying text into the buffer

So, given these 4 keys and N [Number of strokes] needed to findout what is the maximum number of character can be seen in the screen.

example: n=1; only A can be seen bcz only key 1 can be pressed

n=2: only 2 keys can be pressed, so If we pressed 1
time A and later key 2 or 3, or 4 then only 'A'(1) can be seen into the screen but instead of pressing key 2, 3, 4,
If we press 'A' 2 times then we will have 'AA' 2 'A' in the screen


n=3: same as n=2

so, Until n<7: It is best to press only 'A' n times to have maximum 'A' in the screen

if n==7
then
Option: 1 'A' can be pressed 7 times
        2: 'AA' + 2 (select)+3(copy)+4(paste)+4(paste)+4(paste) = 8 [total 8 'A' can be seen in screen]
        3. 'AAA' + 2 (select)+3 copy+4+4= 9 'A' can be seen
        4. 'AAAA' + select + copy + paste = 8 A can be seen

so, recursively:
for each n: A key can be pressed n times: n times
            AA(2)+select(1) +copy(1)+ paste(remaining times of keystrokes: n-4 times)
            AAA(3)+ select(1)+copy(1)+paste(remaining times of key strokes: n-5 times)
            AAAAAAA..A(n-3) + select(1)+copy(1)+paste(1 times)
so f(n) = max(1*n, 2*f(n-4), 3*(n-5)..(n-5)*f(3), (n-4)*f(2), (n-3)*f(1))

so recurslively It can be solved and It will take high complexity bcz same things is being calculating again and again
so, using DP concepts, we can reduce the time complexity for this.



"""


# A Dynamic Programming based Python3 program
# to find maximum number of A's
# that can be printed using four keys

# this function returns the optimal
# length string for N keystrokes
def optimalKeys(N):
    # The optimal string length is
    # N when N is smaller than 7
    if (N <= 6):
        return N

    # An array to store result of
    # subproblems
    screen = [0] * N

    # Initializing the optimal lengths
    # array for until 6 input
    # strokes.

    for n in range(1, 7):
        screen[n - 1] = n

    # Solve all subproblems in bottom manner
    for n in range(7, N + 1):
        # for any keystroke n, we will need to choose between:-
        # 1. pressing Ctrl-V once after copying the
        # A's obtained by n-3 keystrokes.

        # 2. pressing Ctrl-V twice after copying the A's
        # obtained by n-4 keystrokes.

        # 3. pressing Ctrl-V thrice after copying the A's
        # obtained by n-5 keystrokes.
        screen[n - 1] = max(2 * screen[n - 4],
                            max(3 * screen[n - 5],
                                4 * screen[n - 6]))
        # after that recursively find the maximum number A can be printed in the screen.

    return screen[N - 1]


n = 12 # 36
# n=7 # it shows 9
print(optimalKeys(n))
