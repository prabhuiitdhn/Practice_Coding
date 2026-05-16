class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        n = len(s1)

        count = 0
        for i in range(n):
            if s1[i] == s2[i]:
                print("ss:", i)
                continue
            else:
                found_index = 0
                flag = False
                for j in range(i, n):  # finding s1[i] in s2
                    print("s1", s1[i])
                    print("s2", s2[j])
                    if s2[j] == s1[i]:
                        found_index = j
                        print("found:", s1[i])
                        if s2[i] == s1[j]:
                            print("line no 16:", j)
                            list_s = list(s2)
                            list_s[i], list_s[j] = list_s[j], list_s[i]
                            s2 = "".join(list_s)
                            count += 1
                            flag = True
                            break

                if (flag == False):
                    list_s = list(s2)
                    list_s[i], list_s[found_index] = list_s[found_index], list_s[i]
                    s2 = "".join(list_s)
                    # s2[i], s2[found_index] = s2[found_index], s2[i]
                    count += 1

        return count

s = Solution()
s1 = "ababacca"
s2 = "aaabbcca"
print(s.kSimilarity(s1, s2))