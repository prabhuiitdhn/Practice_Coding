# Optimal solution
# Seive of Eratosthenes

class Solution(object):
    def countPrimes(self, n):
        """
        # IT worked but time exceed.
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0

        total_prime = [prime for prime in range(2, n + 1)]
        flag = [True for flag in range(n + 1 - 2)]

        def marked_prime_flag(num):
            current = 2
            while num * current < n + 1:
                if flag[num * current - 2] is True:
                    flag[(num * current) - 2] = False
                current += 1

        if n % 2 == 0:
            total_range = n // 2
        else:
            total_range = (n // 2) + 1

        for i in range(total_range):
            if flag[i] is True:
                marked_prime_flag(total_prime[i])

        current = []
        for j in range(len(total_prime) - 1):
            if flag[j] is True:
                current.append(total_prime[j])

        return len(current)

    def countPrimes2(self, n):
        """
        # It worked but time exceed.
        :type n: int
        :rtype: int
        """

        if n < 3:
            return 0

        total_prime = [True for prime in range(2, n)]

        def marked_prime_flag(num):
            current = 2
            while num * current < n + 1:
                if num * current in total_prime:
                    total_prime.remove(num * current)
                current += 1

        for num in total_prime:
            marked_prime_flag(num)

        return len(total_prime)

    def countPrimes3(self, n):

        # Optimal solution.
        if n<3:
            return 0

        primes = [True for _ in range(n+1)]

        p = 2
        while p*p <= n:
            if primes[p] is True:
                for index in range(p*p, n+1, p):
                    primes[index] = False

            p += 1

        count =0
        for j in range(2, n):
            if primes[j] is True:
                count +=1
        return count


n = 3649
s = Solution()
# print(s.countPrimes2(n))
print(s.countPrimes(n))
print(s.countPrimes3(n))
