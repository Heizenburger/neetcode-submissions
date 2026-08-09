class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = {}
        d2 = {}
        for i, j in zip(s, t):
            d1[i] = 1 + d1.get(i, 0)
            d2[j] = 1 + d2.get(j, 0)
        return d1 == d2