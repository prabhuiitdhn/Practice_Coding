# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
def toh(n, source, destination, temporary):
    # global count
    if n==0:
        return
    toh(n-1, source, temporary, destination)
    print("Move " + str(n) + ' from '+ source +' to '+ destination)
    toh(n-1, temporary, destination, source)
    # count +=1
    # return count

def toh_count(n):
    if n==1:
        return 1
    else:
        return 2*toh_count(n-1)+1

for i in range(t):
    count = 0
    n = int(input())
    print(toh_count(n))
    toh(n, 'A', 'C', 'B')

