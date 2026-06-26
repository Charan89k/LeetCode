class Solution:
    def countMajoritySubarrays(self, nums, target):

        n = len(nums)

        size = 2 * n + 5
        bit = [0] * size

        def update(i):
            while i < size:
                bit[i] += 1
                i += i & -i

        def query(i):
            s = 0
            while i:
                s += bit[i]
                i -= i & -i
            return s

        offset = n + 2
        p = offset

        update(p)

        ans = 0

        for x in nums:
            if x == target:
                p += 1
            else:
                p -= 1

            ans += query(p - 1)
            update(p)

        return ans