class Solution:
  def maxProduct(self, words):
    ans = 0

    def getMask(word):
        # It basically setting the bit on (ord(char)- ord('a'))
        # The bit mask is computed by looping over each character in the string and setting the corresponding bit in the mask to 1.
        # The bit position is determined by subtracting the ASCII value of the character 'a' from the ASCII value of the current character.

      mask = 0
      for c in word:
        mask |= 1 << ord(c) - ord('a')
      return mask

    masks = [getMask(word) for word in words]

    for i in range(len(words)):
      for j in range(i):
        if not (masks[i] & masks[j]):
          ans = max(ans, len(words[i]) * len(words[j]))

    return ans


words = ["abcw","baz","foo","bar","xtfn","abcdef"]
s = Solution()
print(s.maxProduct(words))