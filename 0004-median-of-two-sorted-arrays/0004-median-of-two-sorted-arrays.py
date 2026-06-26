class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2

        l, r = 0, m

        while l <= r:

            i = (l + r) // 2
            j = half - i

            Aleft = float("-inf") if i == 0 else nums1[i - 1]
            Aright = float("inf") if i == m else nums1[i]

            Bleft = float("-inf") if j == 0 else nums2[j - 1]
            Bright = float("inf") if j == n else nums2[j]

            if Aleft <= Bright and Bleft <= Aright:

                if total % 2:
                    return max(Aleft, Bleft)

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0

            elif Aleft > Bright:
                r = i - 1

            else:
                l = i + 1