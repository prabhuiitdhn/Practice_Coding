class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def convertToDecimal(a):
            strlen = len(a)
            power = strlen-1
            in_decimal = 0
            for i in range(strlen):
                if a[i]=='1':
                    in_decimal += 2**(power)
                power -=1

            return in_decimal

        x = convertToDecimal(a)
        print(x)
        y = convertToDecimal(b)
        print(y)

        add = x + y
        return str(bin(add)[2:])

a = '11'
b = '1'
s = Solution()
print(s.addBinary(a, b))