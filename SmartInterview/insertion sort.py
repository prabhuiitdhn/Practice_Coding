class sort(object):
    def insertion(self, nums, n):
        for i in range(1, n):
            current = nums[i]
            j = i - 1
            while j >=0:
                if nums[j] <= current:
                    break
                else:
                    nums[j + 1] = nums[j]
                j -= 1

            nums[j+1] = current
            print(j+1, end = ' ')


# nums = [0, 2, 1, 2, 3, 4]
nums = [176, -272, -272, -45, 269, -327, -945, 176]
s = sort()
s.insertion(nums, len(nums))
print(nums)