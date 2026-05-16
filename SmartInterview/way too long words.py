n = int(input())

for i in range(n):
    word = input()
    word_list = list(word)
    if len(word) >= 10:
        string = word[0] + str(len(word) - 2) + word[-1]
        print(string)
    else:
        print(word)