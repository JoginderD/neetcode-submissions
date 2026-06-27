class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        def isPal(l, r) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        while left < right:
            if s[left] != s[right]:
                if isPal(left, right - 1) or isPal(left + 1, right):
                    return True
                else:
                    return False

            left += 1
            right -= 1

        return True