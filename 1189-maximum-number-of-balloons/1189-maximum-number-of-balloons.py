class Solution:
    def maxNumberOfBalloons(self, text):

        cnt = {}

        for ch in text:
            cnt[ch] = cnt.get(ch, 0) + 1

        return min(
            cnt.get('b', 0),
            cnt.get('a', 0),
            cnt.get('l', 0) // 2,
            cnt.get('o', 0) // 2,
            cnt.get('n', 0)
        )
        