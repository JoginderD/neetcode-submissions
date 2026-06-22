class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = "", ""

        s = s.lower()

        l_int = 0
        r_int = len(s) - 1

        while l_int < r_int:
            
            l = s[l_int]
            r = s[r_int]

            if not s[l_int].isalnum():
                l_int += 1
            elif not s[r_int].isalnum():
                r_int -= 1
            else :
                if l == r:
                    l_int += 1
                    r_int -= 1
                else:
                    return False
        
        return True
        