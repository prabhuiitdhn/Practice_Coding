
def roundToNearest(N):
    division = int(int(N)//10)
    if int(N)%10>5:
        return 10*(division+1)
    else:
        return 10*division
    # return

# N ="29"
N ="8612455638334947271564617487839781"
print(roundToNearest(N))