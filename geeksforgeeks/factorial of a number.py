

def factorial(n):
    def factorial_helper(n):
        if n == 1:
            return 1
        return n * factorial_helper(n - 1)
    value = factorial_helper(n)
    output = []
    value = list(str(value))
    for i in range(len(value)):
        output.append(int(value[i]))

    print(output)

n =10
print(factorial_helper(n))