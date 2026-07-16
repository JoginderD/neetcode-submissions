class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        l, r = 0, 0
        check = set()

        while r < len(s):

            if s[r] in check:
                check = set()
                r = l + 1
                l += 1
            else:
                check.add(s[r])
                r += 1


            m = max(m, r - l)
        
        return m