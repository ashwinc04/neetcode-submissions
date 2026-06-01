class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        ns = set(nums)
        # (2, 20, 3, 10, 4, 5)
        for a in ns:
            if (a-1) not in ns:
                tmp = 0
                while a in ns:
                    a = a+1
                    tmp = tmp + 1
                if tmp > count:
                    count = tmp
            else:
                pass
        return count
