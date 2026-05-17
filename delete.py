x =[1, 2, 3, 4]
y = [i**2 for i in x]
print(y)

y = [j+1 for j in [i**2 for i in x]]
print(y)

y = [j+1 for j in [i**2 for i in x] if j%2==0 else j+2]
print(y)